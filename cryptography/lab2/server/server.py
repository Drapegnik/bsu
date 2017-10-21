import os
import uuid

from flask import Flask

from settings import APP_STATIC
from utils import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login', methods=['POST'])
def login():
    session_key = uuid.uuid4()
    return json(session_key)


@app.route('/data')
def get_data():
    with open(os.path.join(APP_STATIC, 'data.txt')) as f:
        return json(f.read())


if __name__ == '__main__':
    app.run()
