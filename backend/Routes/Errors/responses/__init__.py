#!/usr/bin/env python3
from flask import make_response
from flask import jsonify

class Response:
    def __new__(self, statusCode, data):
        return make_response(jsonify(data), statusCode)

