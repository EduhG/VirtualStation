from flask import Flask
from config import config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.config.from_pyfile('config.py')

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
