from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Working on User Authenication
from flask_bcrypt import Bcrypt




capstone_app = Flask(__name__)

bcrypt = Bcrypt(capstone_app)


ENV = 'dev'

if ENV == 'dev':
    capstone_app.debug = True
    capstone_app.config.from_pyfile('settings.py')
else:
    capstone_app.debug = False
    capstone_app.config.from_pyfile('settings.py')


capstone_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(capstone_app)

from capstone import routes