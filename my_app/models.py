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
    
 
 
class Department(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(length=30),nullable=False)
    manager_id= db.Column(db.Integer(),unique=True)

    #relationship fields
    rel_id_dept = db.relationship('Users',backref='rel_id_dept',lazy=True)
    
    create_uid = db.Column(db.Integer())
    write_uid = db.Column(db.Integer())
    creation_date = db.Column(db.Date(),nullable=False)
    write_date =  db.Column(db.Date(),nullable=False)
    
 

class Users(db.Model,UserMixin):
    id = db.Column(db.Integer(),primary_key=True)
    
    firstname=db.Column(db.String(length=30),nullable=False)
    lastname=db.Column(db.String(length=30),nullable=False)
    email_address=db.Column(db.String(length=50),nullable=False,unique=True)
    password_hash=db.Column(db.String(length=30),nullable=False)
    
    
    #relationship fields
    rel_id_jobs = db.relationship('Jobs',backref='rel_id_jobs',lazy=True)
    department_id =db.Column(db.Integer(),db.ForeignKey('department.id'))
    user_type_id = db.Column(db.Integer(),db.ForeignKey('usertype.id'))
    
    creation_date = db.Column(db.Date(),nullable=False)
    write_date =  db.Column(db.Date(),nullable=False)
    


    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrpt.generate_password_hash(plain_text_password).decode('utf-8')
    
    
    def check_password_correction(self,attempted_password):
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
    

    