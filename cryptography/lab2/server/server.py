import os
from time import time

from flask import Flask, request

from crypto import rsa, aes
from settings import APP_STATIC
from utils import json, get_session_key, SESSION_KEY_EXPIRATION_TIME

app = Flask(__name__)

db = {
    'admin': {
        'password': 'secret'
    },
    'bob': {
        'password': 'foo'
    },
    'alice': {
        'password': 'bar'
    }
}


def key_expired(created_at):
    return (time() - created_at) > SESSION_KEY_EXPIRATION_TIME


@app.route('/login', methods=['POST'])
def login():
    body = request.get_json()
    user, password = body.get('user'), body.get('password')
    if not db.get(user, {}).get('password') == password:
        return json(None, 'Incorrect login or password!'), 401
    try:
        pub_key = int(body['key']['e']), int(body['key']['n'])
    except ValueError:
        return json(None, 'PublicKey(e, n) should consist of two integers!'), 400

    session_key = get_session_key(aes.KEY_LENGTH)
    encrypted_key = rsa.encrypt(pub_key, session_key)
    if __debug__:
        print('SESSION_KEY:', session_key)

    db[user]['session_key'] = session_key
    db[user]['created_at'] = time()
    return json({'sessionKey': encrypted_key})


@app.route('/data', methods=['POST'])
def get_data():
    body = request.get_json()
    user = db.get(body['user'], {})

    if not user.get('session_key') or key_expired(user.get('created_at')):
        return json(None, 'Session key has expired!'), 401

    session_key = user['session_key']

    with open(os.path.join(APP_STATIC, 'data.txt'), 'rb') as f:
        data = list(f.read())
        encrypted_data = aes.encrypt(data, session_key)
        if __debug__:
            decrypted_data = aes.decrypt(encrypted_data, session_key)
            print('ENCRYPTION CORRECT:', bytes(decrypted_data).startswith(bytes(data)))

        return json({'encrypted': encrypted_data})


"""
Private api for sharing crypto methods with client, to avoid code duplicating
(I don't want to implement algorithms also on javascript)
"""


@app.route('/private/rsa/generate', methods=['POST'])
def get_rsa_keys():
    body = request.get_json()
    try:
        public, private = rsa.generate_keypair(int(body['p']), int(body['q']))
    except ValueError as error:
        return json(None, str(error)), 400
    e, n = public
    d, n = private
    return json({'e': e, 'd': d, 'n': n})


@app.route('/private/rsa/decrypt', methods=['POST'])
def rsa_decrypt():
    body = request.get_json()
    try:
        priv_key = int(body['key']['d']), int(body['key']['n'])
    except ValueError:
        return json(None, 'PrivateKey(d, n) should consist of two integers!')
    data = body['data']
    return json({'decrypted': rsa.decrypt(priv_key, data)})


@app.route('/private/aes/decrypt', methods=['POST'])
def aes_decrypt():
    body = request.get_json()
    encrypted, session_key = body['encrypted'], body['key']
    decrypted_data = bytes(aes.decrypt(encrypted, session_key)).decode('utf-8', 'ignore')
    return json({'text': decrypted_data})


if __name__ == '__main__':
    app.run()
