import os

from api.db import SQLAlchemy

# Declare your config classes with settings variables here
class Config:
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    SECRET_KEY = os.environ.get('SECRET_KEY', 'My Secret')

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',
            'sqlite:///jetcake.db')
    TEST_SQLALCHEMY_DATABASE_URI = os.environ.get(
            'TEST_SQLALCHEMY_DATABASE_URI', 'sqlite:///jetcake_test.db'
    )

class ProductionConfig(Config):
    pass

ENV_MAPPING = {
    'DEVELOPMENT': DevelopmentConfig,
    'PRODUCTION': ProductionConfig
}

# Globals. If you like move it to separate module
db = SQLAlchemy(autocommit=True)
config = ENV_MAPPING[os.environ.get('API_ENV', 'DEVELOPMENT')]
