import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
  DEBUG = bool(os.getenv('DEBUG', 0))
  TESTING = bool(os.getenv('TESTING', 0))
  PRESERVE_CONTEXT_ON_EXCEPTION = not TESTING

key = Config.SECRET_KEY