import os

# Makes the token an environment variable for security reasons

#Create secret key for WTF-forms

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'development-key'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace(
        'postgres://', 'postgresql://') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

# class ProductionConfig(Config):
#     ENV='production'
#     SECRET_KEY = os.environ['SECRET_KEY']
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','').replace('postgres://', 'postgresql://') or 'sqlite:///' + os.path.join(basedir, 'app.db')

# class DevelopmentConfig(Config):
#     FLASK_ENV='development'
#     DEBUG=True

# class TestingConfig(Config):
#   ENV='testing'
#   SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'tests/test.db')
#   #SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:' #in memory database
  


 

