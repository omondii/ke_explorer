#!/usr/bin/env python3
from flask import make_response, jsonify
from flask import Blueprint

# Register routes as blueprints
app_views = Blueprint('app_views', __name__, template_folder='templates')
from . import views

