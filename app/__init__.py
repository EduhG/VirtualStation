from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
import logging
import sys

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.signin'


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    # app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.config.from_pyfile('config.py', silent=True)

    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.ERROR)

    db.init_app(app)
    login_manager.init_app(app)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .dashboard import dashboard as dashboard_blueprint
    app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')

    return app
