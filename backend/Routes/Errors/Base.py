#!/usr/bin/env python3
"""
A custom exseption handler class that inherits from pythons Exception class
"""
from http import HTTPStatus
from flask import current_app
from flask import jsonify


class BaseExceptionHandler(Exception):
    statusCode = None
    message = None
    error_code = None

    def __init__(self, public=None, debug=None, details=None):
        self.public = public
        self.debug = debug
        self.details = details
        self._log()

    @property
    def errors(self):
        return {
            "message": self.public or self.default_message,
            "status": HTTPStatus(self.statusCode).phrase,
            "statusCode": self.statusCode
        }

    def _log(self):
        if self.debug is None:
            return

        if isinstance(self.debug, list):
            for item in self.debug:
                if item is not None:
                    current_app.logger.debug(f"{type(self).__name__} - {item}")
        elif isinstance(self.debug, dict):
            current_app.logger.debug(f"{type(self).__name__} - {str(self.debug)}")
        else:
            current_app.logger.debug(f"{type(self).__name__} - {str(self.debug)}")


class BaseSuccessHandler(Exception):
    statusCode = None
    default_message = None
    code = None

    def __init__(self, public=None, debug=None, details=None):
        self.public = public
        self.debug = debug
        self.details = details

    @property
    def response(self):
        return jsonify({
            "status": "success",
            "message": self.default_message,
            "statusCode": self.statusCode,
            "data": self.details
        })

