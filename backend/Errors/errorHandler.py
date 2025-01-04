#!/usr/bin/env python3
from http import HTTPStatus
import traceback
import json
from flask import current_app, Response
from Errors.Base import BaseExceptionHandler
from Errors import CustomResponse


def error_handler(exception):
    if isinstance(exception, BaseExceptionHandler):
        error_data = {
            "message": exception.public or exception.default_message,
            "status": HTTPStatus(exception.statusCode).phrase,
            "statusCode": exception.statusCode
        }

        # return Response(
        #     json.dumps(error_data),
        #     status=exception.statusCode,
        #     mimetype='application/json'
        # )

    current_app.logger.error(f"{type(exception).__name__} - {exception}")
    if current_app.debug:
        current_app.logger.error(traceback.format_exc())

    # Generic server Response
    error_response = {
        "status": "Server Error",
        "message": "An unexpected Error Occurred",
        "statusCode": 500
    }

    return CustomResponse.create(
        statusCode=500,
        data = error_response
    )

