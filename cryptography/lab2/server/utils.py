import random

from flask import jsonify


SESSION_KEY_EXPIRATION_TIME = 30  # seconds
s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


def get_session_key(length):
    return ''.join(random.sample(s, length))


def json(data, error=None):
    return jsonify(data=data, error=error)
