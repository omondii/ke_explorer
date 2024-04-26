#!/usr/bin/env python3
""" View functions for user authentication 
Flask jwt module used"""
import json
from flask import jsonify, request
from server import app
from Auth import auth
from flask_jwt_extended import create_access_token, unset_jwt_cookies, \
    get_jwt, get_jwt_identity, jwt_required
from datetime import datetime, timezone, timedelta



@auth.after_request
def refresh_expiring_jwts(response):
    """ Prevents token expiration while user is logged in
    Will refresh the tokens once the set Expiry is achieved"""
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data['access_token'] = access_token
                response.data = json.dumps(data)
        return response
    except (RuntimeError, KeyError):
        return response

@auth.route('/token', methods=['POST'])
def create_token():
    """ Extracts user email and password upon a login attempt
    If the details are correct, a jwt access token is created """
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "test" or password != "test":
        return {"msg": "Wrong Email or Password"}, 401
    
    access_token = create_access_token(identity=email)
    response = {"access_token": access_token}
    return response

@auth.route('/profile')
@jwt_required()
def my_profile():
    """ Contains currently logged in users profile details """
    response_body = {
        "name": "Brian",
        "about": "Welcome To ExporeKe"
    }
    return response_body

@auth.route('/logout', methods=['POST'])
def logout():
    """ When a logout request is submitted, the unset..cookies deletes
    the cookies containing the access token"""
    response = jsonify({"msg": "Logged Out!"})
    unset_jwt_cookies(response)
    return response