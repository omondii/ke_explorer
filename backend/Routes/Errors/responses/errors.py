#!/usr/bin/env python3
from http import HTTPStatus
from Routes.Errors.Base import BaseExceptionHandler, BaseSuccessHandler

class ResponseFactory:
    """ Error responses generation class """

    @staticmethod
    def create_exception(exception_class, public=None, debug=None, details=None):
        return exception_class(public=public, debug=debug, details=details)


    @classmethod
    def authentication_error(cls, public=None, debug=None, details=None):
        class AuthenticationError(BaseExceptionHandler):
            statusCode = HTTPStatus.UNAUTHORIZED
            default_message = "Authentication Failed"
            error_code = "Auth Error"
        return cls.create_exception(AuthenticationError, public=public, debug=debug, details=details)

    @classmethod
    def validation_error(cls, public=None, debug=None, details=None):
        class ValidationError(BaseExceptionHandler):
            statusCode = HTTPStatus.BAD_REQUEST
            default_message = "Invalid Input"
            error_code = "VALIDATION_ERROR"
        return cls.create_exception(ValidationError, public=None, debug=debug, details=details)

    @classmethod
    def not_found_error(cls, resource=None, debug=None, details=None):
        class NotFoundError(BaseExceptionHandler):
            statusCode = HTTPStatus.NOT_FOUND
            default_message = f"{resource} not found"
            error_code = "NOT_FOUND"
        return cls.create_exception(NotFoundError, public=None, debug=debug, details=details)

    @classmethod
    def user_exists_error(cls, resource=None, public=None, debug=None, details=None):
        class ConflictError(BaseExceptionHandler):
            statusCode = HTTPStatus.CONFLICT
            default_message = f"{resource} already exists!"
            error_code = "CONFLICT"
        return cls.create_exception(ConflictError, public=public, debug=debug, details=details)

    @classmethod
    def resource_created(cls, resource, data=None, debug=None):
        class Success(BaseSuccessHandler):
            statusCode = HTTPStatus.CREATED
            default_message = f"{resource} Created Successfully"
            code = "CREATED"
        return cls.create_exception(Success, public=None, debug=debug, details=data)

    @classmethod
    def invalid_request(cls, public=None, debug=None, details=None):
        class Invalid(BaseExceptionHandler):
            statusCode = HTTPStatus.INVALID_REQUEST
            default_message = "Invalid Request"
            error_code = "INVALID"
        return cls.create_exception(Invalid, public=None, debug=None, details=None)

