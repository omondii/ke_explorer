#!/usr/bin/env python3
import traceback
import json
from flask import current_app, Response
from Routes.Errors.Base import BaseExceptionHandler
from Routes.Errors.responses import Response


def error_handler(exception):
    if isinstance(exception, BaseExceptionHandler):
        return Response(
            response = json.dumps(exception.error_response),
            status  = exception.statusCode,
            mimetype = 'application/json'
        )

    current_app.logger.error(f"{type(exception).__name__} - {exception}")
    if current_app.debug:
        current_app.logger.error(traceback.format_exc())

    # Generic server Response
    error_response = {
        "error": {
            "code": "Server Error",
            "message": "An unexpected Error Occured",
            "statusCode": 500
        }
    }

    return Response(
        response=json.dumps(error_response),
        status=500,
        mimetype='application/json'
    )

