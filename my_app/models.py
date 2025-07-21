from my_app import db,login_manager
from my_app import bcrpt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))




class Usertype(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(length=30),unique=True,nullable=False)
    #relationship fields
    user_type=db.relationship('Users',backref='desig_user',lazy=True)
    
    def __str__(self):
        return self.name
 
 
class Department(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(length=30),nullable=False)
    manager_id= db.Column(db.Integer(),unique=True)

    #relationship fields
    department = db.relationship('Users',backref='desig_dept',lazy=True)
    
    manager_id= db.Column(db.Integer())
    color = db.Column(db.String(length=30),nullable=False)
    
    create_uid = db.Column(db.Integer())
    write_uid = db.Column(db.Integer())
    creation_date = db.Column(db.Date(),nullable=False)
    write_date =  db.Column(db.Date(),nullable=False)
    
 

class Users(db.Model,UserMixin):
    id = db.Column(db.Integer(),primary_key=True)
    firstname=db.Column(db.String(length=30),nullable=False)
    lastname=db.Column(db.String(length=30),nullable=False)
    email_address=db.Column(db.String(length=51),nullable=False)
    password_hash=db.Column(db.String(length=30),nullable=False)
    
    address_1 = db.Column(db.String(length=120),nullable=True)
    address_2 = db.Column(db.String(length=100),nullable=True)
    brgy_id = db.Column(db.String(),nullable=True)
    munci_id = db.Column(db.String(),nullable=True)
    prov_id = db.Column(db.String(),nullable=True)
    zipcode = db.Column(db.String(),nullable=True)
    
    mobile_number = db.Column(db.String(length=11),nullable=True)
    phone_number = db.Column(db.String(length=8),nullable=True)
    profile_picture =db.Column(db.String(),nullable=True)
    
    #relationship fields
    department_id =db.Column(db.Integer(),db.ForeignKey('department.id'))
    department = db.relationship('Department')
    
    
    user_type_id = db.Column(db.Integer(),db.ForeignKey('usertype.id'))
    user_type = db.relationship('Usertype')
    
    
    
    creation_date = db.Column(db.Date(),nullable=False)
    write_date =  db.Column(db.Date(),nullable=False)
    
    
    @property
    def password(self):
        # self.password
        raise AttributeError("Password is write-only.")
        
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrpt.generate_password_hash(plain_text_password).decode('utf-8')
    
    
    def check_password_correction(self,attempted_password):
        # print('check password correction')
        return bcrpt.check_password_hash(self.password_hash,attempted_password)
            


    



class Jobs(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    job_title=db.Column(db.String(length=30),nullable=False)
    employment_type=db.Column(db.String(length=15),nullable=False)
    min_sal= db.Column(db.Float(),nullable=False)
    max_sal= db.Column(db.Float(),nullable=False)
    start_date = db.Column(db.Date(),nullable=False)
    location =db.Column(db.String(length=50),nullable=False)
    description =db.Column(db.String(length = 1030), nullable=False, unique=True)
    start_date = db.Column(db.Date(),nullable=False)
    
    #relationship fields
    department_id =db.Column(db.Integer, db.ForeignKey('department.id'))
    user_uid = db.Column(db.Integer(),db.ForeignKey('users.id'))
    
    create_uid = db.Column(db.Integer())
    write_uid = db.Column(db.Integer())
    creation_date = db.Column(db.Date(),nullable=False)
    write_date =  db.Column(db.Date(),nullable=False)
    
