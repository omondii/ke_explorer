#!/usr/bin/env python3
from http import HTTPStatus
from Routes.Errors.Base import BaseExceptionHandler

class ErrorResponseFactory:
    """ Error responses generation class """

    @staticmethod
    def create_exception(exception_class, public=None, debug=None, details=None):
        return exception_class(public=public, debug=debug, details=details)


    @classmethod
    def authentication_error(cls, message=None, debug=None, details=None):
        class AuthenticationError(BaseExceptionHandler):
            statusCode = HTTPStatus.UNAUTHORIZED
            default_message = "Authentication Failed"
            error_code = "Auth Error"
        return cls.create_exception(AuthenticationError, message, debug, details)

    @classmethod
    def validation_error(cls, resource=None, debug=None, details=None):
        class ValidationError(BaseExceptionHandler):
            statusCode = HTTPStatus.BAD_REQUEST
            default_message = "Invalid Input"
            error_code = "VALIDATION_ERROR"
        return cls.create_exception(ValidationError, message, debug, details)

    @classmethod
    def not_found_error(cls, resource=None, debug=None, details=None):
        class NotFoundError(BaseExceptionHandler):
            statusCode = HTTPStatus.NOT_FOUND
            default_message = f"{resource} not found"
            error_code = "NOT_FOUND"
        return cls.create_exception(NotFoundError, None, debug, details)

    @classmethod
    def user_exists_error(cls, resource=None, debug=None, details=None):
        class ConflictError(BaseExceptionHandler):
            status_code = HTTPStatus.CONFLICT
            default_message = f"{resource} already exists!"
            error_code = "CONFLICT"

        return cls.create_exception(ConflictError, public=details, debug=debug, details=None)

    @classmethod
    def resourceCreated(cls, resource, debug=None, details=None):
        pass

