from flask import Flask
import flask_admin
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_app_db.db'
app.config['SECRET_KEY'] = 'b5b6981766a5bbbd3c901b1e'

db = SQLAlchemy(app)

bcrpt= Bcrypt(app)






login_manager =LoginManager(app) #this line is for LoginManager initialize by installing flask_login via pip and import it above
login_manager.login_view = "login_page" # type: ignore
login_manager.login_message_category = "primary"


from my_app import routes