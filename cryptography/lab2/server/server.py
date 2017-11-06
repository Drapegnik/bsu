import os

from flask import Flask, request

from crypto import rsa
from settings import APP_STATIC
from utils import json, get_session_key

app = Flask(__name__)
SESSION_KEY_LENGTH = 6


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/data', methods=['POST'])
def get_data():
    try:
        pub_key = int(request.form['e']), int(request.form['n'])
    except ValueError:
        return json(None, 'Error: PublicKey(e, n) should consist of two integers!')
    session_key = rsa.encrypt(pub_key, get_session_key(SESSION_KEY_LENGTH))
    with open(os.path.join(APP_STATIC, 'data.txt')) as f:
        return json({
            'key': session_key,
            'text': f.read()
        })


if __name__ == '__main__':
    app.run()
