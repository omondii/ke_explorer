#!/usr/bin/env python3
from flask import make_response, jsonify

class CustomResponse:
    @staticmethod
    def create(statusCode, data):
        return make_response(jsonify(data), statusCode)

