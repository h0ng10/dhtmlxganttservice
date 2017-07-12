from flask import Blueprint

gantt = Blueprint('gantt', __name__)

from . import views
