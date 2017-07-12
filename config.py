import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you_should_really_change_me'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    HOST = '0.0.0.0'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'ganttservice-dev.sqlite3')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'ganttservice-test.sqlite3')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'ganttservice.sqlite3')

config = {
 'development': DevelopmentConfig,
 'testing': TestingConfig,
 'production': ProductionConfig,
 'default': DevelopmentConfig
}
