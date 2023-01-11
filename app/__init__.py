from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_mail import Mail
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging, os


app = Flask(__name__)

app.config.from_object(Config)
app.config.from_object('config.ProductionConfig')
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://xvgcrkgyqhioyd:1b70e8869d3d6451e817962d41046ac35c28cde8189bae8c2da40ac938d6c191@ec2-54-157-79-121.compute-1.amazonaws.com:5432/dev1re8boq3p3u"

mail = Mail(app)
db = SQLAlchemy(app)
Migrate(app, db)


# def create_app(config_class=Config):
#     # ...
#     if not app.debug and not app.testing:
#         # ...

#         if app.config['LOG_TO_STDOUT']:
#             stream_handler = logging.StreamHandler()
#             stream_handler.setLevel(logging.INFO)
#             app.logger.addHandler(stream_handler)
#         else:
#             if not os.path.exists('logs'):
#                 os.mkdir('logs')
#             file_handler = RotatingFileHandler('logs/paulineg.log',
#                                                maxBytes=10240, backupCount=10)
#             file_handler.setFormatter(logging.Formatter(
#                 '%(asctime)s %(levelname)s: %(message)s '
#                 '[in %(pathname)s:%(lineno)d]'))
#             file_handler.setLevel(logging.INFO)
#             app.logger.addHandler(file_handler)

#         app.logger.setLevel(logging.INFO)
#         app.logger.info('paulineg startup')

#     return app

from app import routes





