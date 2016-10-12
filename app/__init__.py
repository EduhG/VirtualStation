from flask import Flask
import logging
import sys
from config import config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    # app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.config.from_pyfile('config.py', silent=True)

    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.ERROR)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
