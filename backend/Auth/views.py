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
from Routes.Errors.responses.errors import ErrorResponseFactory


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
                return jsonify({
                    "status": "Bad Request",
                    "message": "Missing Fields",
                    "statusCode": 400
                }), 400

            # Check if user already registered
            existing_user = storage.get_by_email(User, email)
            if existing_user:
                raise ErrorResponseFactory.user_exists_error(
                    resource = "User",
                    debug={
                        "email": email,
                        "user_id": existing_user.id
                    },
                    details="A user with this email address is already registered"
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

            return jsonify({
                "status": "success",
                "message": "Registration successful",
                "statusCode": 201,
                "data": {
                    "accessToken": access_token,
                    "user": {
                        "userId": user.id,
                        "username": user.username,
                        "email": user.email,
                    }
                }
            }), 201

        except Exception as e:
            storage.rollback()
            return jsonify({
                "status": "Bad request",
                "message": str(e),
                "statusCode": 400
            }), 400

    return jsonify({
        "status": "Bad request",
        "message": "Invalid request",
        "statusCode": 401
    }), 401


@auth.route('/login', methods=['POST'])
def login():
    """ User system login
    """
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    # Check for missing input
    if not all([email, password]):
      return jsonify({
        "status": "Bad Request",
        "message": "Missing a field",
        "StatusCode": 400
      }), 400

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
         return jsonify({
          "status": "Unauthorized",
          "message": "Authentication failed",
          "statusCode": 401
      }), 401

