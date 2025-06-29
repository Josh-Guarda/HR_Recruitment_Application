from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
import json

app = Flask(__name__)

#BASE CONFIG
app.config.from_pyfile("config.py")

#UPLOADS
UPLOAD_FOLDER = 'C:/Users/JoshuaPC/Desktop/FLASK_RECRUITMENT/my_app/static/uploads/avatars' #Note: make this as the absolute file path on your machine or server directory to avoid FileNotFoundError: [Errno 2] No such file or directory:
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#Directory of JSON FILES
Barangay_JSON='my_app/static/json/ref_brgy.json'
Municipality_JSON='my_app/static/json/ref_city_mun.json'
Province_JSON='my_app/static/json/ref_province.json'

#OPEN JSON file to extract RECORDS (THIS will be called to routes.py)
with open('my_app/static/json/ref_brgy.json', encoding='utf-8') as f:
    BARANGAY_DATA = json.load(f)['RECORDS']

with open('my_app/static/json/ref_city_mun.json', encoding='utf-8') as f:
    MUNICIPALITY_DATA = json.load(f)['RECORDS']

with open('my_app/static/json/ref_province.json', encoding='utf-8') as f:
    PROVINCE_DATA = json.load(f)['RECORDS']



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