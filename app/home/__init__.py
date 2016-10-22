from flask import Blueprint

home = Blueprint('home', __name__)

from . import views, errors
from app.auth.models import Permission


@home.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
