from flask import Blueprint

app_views = Blueprint('app_views', __name__, template_folder='templates')

from . import views