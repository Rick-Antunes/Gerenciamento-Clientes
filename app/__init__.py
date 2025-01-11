from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import login_required, LoginManager
import os


#-----#-----#-----#-----#-----#-----#
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///celulasdecafe.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'feahifheaifhseuifonsaefjneafuihefua'

db = SQLAlchemy(app)
migrate = Migrate(app,db)

bcrypt = Bcrypt(app)

#login_manager = LoginManager(app)
#login_manager.init_app(app)

from app.views import indexPage, cadastroPage