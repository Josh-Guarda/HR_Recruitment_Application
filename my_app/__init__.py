from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)
#BASE CONFIG
app.config.from_pyfile("config.py")
#UPLOADS
UPLOAD_FOLDER = 'static/uploads/avatars'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#SQL DB
db = SQLAlchemy(app)
#ENCRYPTING for PW
bcrpt= Bcrypt(app)

#MIGRATE from flask_migrate for any additional column to define in sqlalchemy
migrate = Migrate(app, db)  


login_manager =LoginManager(app) #this line is for LoginManager initialize by installing flask_login via pip and import it above
login_manager.login_view = "login_page" # type: ignore
login_manager.login_message_category = "primary"




from my_app import routes