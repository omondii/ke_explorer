#!/usr/bin/env python3
# Custom Error builder
class CustomResponse:
    @staticmethod
    def create(statusCode, data):
        return make_response(jsonify(data), statusCode)

