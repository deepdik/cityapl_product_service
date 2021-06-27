import os
from .credentials import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 


class Config:
    """Base config."""    
    STATIC_FOLDER = 'static'
    TESTING = False
    DEBUG = False
    SECRET_KEY = SECRET_KEY
    PORT = '5000'


class ProdConfig(Config):
    """
    Production configuration
    """
    FLASK_ENV = 'production'
    ENV = 'production'
    DATABASE = DATABASES['postgres']


class DevConfig(Config):
    """
    Development configuration
    """
    FLASK_ENV = 'development'
    ENV = 'development'
    DEBUG = True
    DATABASE = DATABASES['postgres']
    

class TestConfig(Config):
    """
    Testing configuration
    """
    FLASK_ENV = 'development'
    ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE = DATABASES['testing']