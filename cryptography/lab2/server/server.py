import os

from flask import Flask, request

from crypto import rsa, aes
from settings import APP_STATIC
from utils import json, get_session_key

app = Flask(__name__)


@app.route('/data', methods=['POST'])
def get_data():
    try:
        pub_key = int(request.form['e']), int(request.form['n'])
    except ValueError:
        return json(None, 'Error: PublicKey(e, n) should consist of two integers!')

    session_key = get_session_key(aes.KEY_LENGTH)
    encrypted_key = rsa.encrypt(pub_key, session_key)
    if __debug__:
        print('SESSION_KEY:', session_key)
    with open(os.path.join(APP_STATIC, 'data.txt'), 'rb') as f:
        data = list(f.read())
        encrypted_data = aes.encrypt(data, session_key)
        if __debug__:
            decrypted_data = aes.decrypt(encrypted_data, session_key)
            print('ENCRYPTION CORRECT:', bytes(decrypted_data).startswith(bytes(data)))

        return json({
            'key': encrypted_key,
            'text': encrypted_data
        })


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
        print(error)
        return json(None, 'Something went wrong!')
    e, n = public
    d, n = private
    return json({'e': e, 'd': d, 'n': n})


if __name__ == '__main__':
    app.run()
