#!/usr/bin/env python3
""" Application entry point from flask import Flask """
from flask import Flask
from flask_cors import CORS
#from config import Config
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    CORS(app, resources={'r/backend/*': {'origins': 'http://localhost:5000'}})
    #app.config.from_object(Config)
    login = LoginManager(app)

    # Register Blueprints
    from Auth import auth
    app.register_blueprint(auth)

    from Routes import app_views
    app.register_blueprint(app_views)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)