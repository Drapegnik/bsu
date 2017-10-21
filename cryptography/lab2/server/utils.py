from flask import jsonify


def json(data):
    return jsonify({'data': data})
