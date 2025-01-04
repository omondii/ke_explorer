#!/usr/bin/env python3
"""
User Profile creation and management backend
"""
from flask import request, jsonify
from Auth import auth
from Models import storage
from .utils import generate_token
import uuid
from Models.tables import User
from werkzeug.security import check_password_hash
from Routes.Errors.responses.errors import ResponseFactory


@auth.route('/register', methods=['POST'])
def register():
    """Create a new user"""
    if request.method == 'POST':
        try:
            data = request.get_json()

            name = data.get('username')
            email = data.get('email')
            password = data.get('password')

            # Validate input
            if not all([name, email, password]):
                raise ResponseFactory.validation_error(
                    resource="User",
                    debug={
                        "email": email,
                        "name": name
                    },
                    details = "Missing a required Field"
                )

            # Check if user already registered
            existing_user = storage.get_by_email(User, email)
            if existing_user:
                raise ResponseFactory.user_exists_error(
                    resource = "User",
                    public="Kindly Check your details and try again",
                    debug={
                        "email": email,
                        "user_id": existing_user.id
                    },
                    details="Email already in use"
                )

            # New user instance to save user to DB
            user = User(
                id=str(uuid.uuid4()),
                username=name,
                email=email,
                password=password
            )
            storage.new(user)
            storage.save()
            access_token = generate_token(user.id)

            response_data = {
                "accessToken": access_token,
                "user": {
                    "userId": user.id,
                        "username": user.username,
                        "email": user.email,
                }
            }

            raise ResponseFactory.resource_created(
                resource = "User",
                data = response_data
            ).response

        except Exception as e:
            storage.rollback()
            return e.errors, e.statusCode

    raise ResponseFactory.invalid_request(
        public = "Invalid Request",
    )


@auth.route('/login', methods=['POST'])
def login():
    """ User system login
    """
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    # Check for missing input
    if not all([email, password]):
      raise ResponseFactory.validation_error(
            resource="User",
            debug={
                "email": email,
                "name": name
            },
            details = "Missing a required Field"
        )

    # Retrieve user
    user = storage.get_by_email(User, email)

    if user and check_password_hash(user.password, password):
      # Create access token
      # access_token = generate_token(user.id)

      return jsonify({
          "status": "Success",
          "message": "Login Successful",
          "statusCode": 200,
          "data": {
              "accessToken": access_token,
              "user": {
                  "userId": user.id,
                  "username": user.username,
                  "email": user.email,
              }
          }
      }), 200
    else:
         raise ResponseFactory.authentication_error(
            public = "Authenticate To View This Page"
         )

