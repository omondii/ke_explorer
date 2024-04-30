#!/usr/bin/env python3
""" Application entry point from flask import Flask """
import os
from flask import Flask
from flask_cors import CORS # type: ignore
from config import Config
from flask_login import LoginManager # type: ignore
from flask_jwt_extended import JWTManager  # type: ignore
from datetime import datetime, timedelta, timezone


app = None
def create_app():
    global app
    app = Flask(__name__)
    CORS(app, resources={'r/backend/*': {'origins': 'http://localhost:5000'}})
    app.config.from_object(Config)
    app.secret_key = os.environ.get('JWT_SECRET_KEY')
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    JWTManager(app)
    
    # Register Blueprints
    from Auth import auth
    app.register_blueprint(auth)

    from Routes import app_views
    app.register_blueprint(app_views)

    return app

if __name__ == '__main__':
    create_app()
    app.run(debug=True)