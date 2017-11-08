import os

from flask import Flask, request

from crypto import rsa, aes
from settings import APP_STATIC
from utils import json, get_session_key

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


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


if __name__ == '__main__':
    app.run()
