from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_app_db.db'

db = SQLAlchemy(app)

# app.app_context().push()
from my_app import routes  #importing routes to run in __init__ since routes are in routes.py file