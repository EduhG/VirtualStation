# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    THREADS_PER_PAGE = 2
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
        'yiwj\xfa\xe0\x18\xe7\xde\xa1\x8b#\x9e\xdbyXqC\x9e\xcdK\xcaz8'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = os.environ.get('SECRET_KEY') or \
        'yiwj\xfa\xe0\x18\xe7\xde\xa1\x8b#\x9e\xdbyXqC\x9e\xcdK\xcaz8'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    VS_MAIL_SUBJECT_PREFIX = '[Virtual Station]'
    VS_MAIL_SENDER = 'Virtual Station Admin <vs@example.com>'
    VS_ADMIN = os.environ.get('VS_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'virtual_station.db')
    DATABASE_CONNECT_OPTIONS = {}


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'vs_test.db')
    DATABASE_CONNECT_OPTIONS = {}


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    DATABASE_CONNECT_OPTIONS = {}
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
