from my_app import db



class Usertype(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(length=30),unique=True,nullable=False)
    
    user_type=db.relationship('Users',backref='desig_user',lazy=True)
    
 
 
class Department(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(length=30),nullable=False)
    manager_id= db.Column(db.Integer(),unique=True)

    #other fields
    user_id = db.Column(db.Integer(),db.ForeignKey('users.id'))
    
    
    create_uid = db.Column(db.Integer())
    write_uid = db.Column(db.Integer())
    creation_date = db.Column(db.Date(),nullable=False)
    write_date =  db.Column(db.Date(),nullable=False)
    
 
 
class Users(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(length=30),unique=True,nullable=False)
    password_hash=db.Column(db.String(length=30),nullable=False)
    email_address=db.Column(db.String(length=50),nullable=False,unique=True)
    department =db.Column(db.String(length=30),nullable=False)
    
    
    rel_id_dept = db.relationship('Department',backref='rel_id_dept',lazy=True)
    rel_id_jobs = db.relationship('Jobs',backref='rel_id_jobs',lazy=True)
    user_type_id = db.Column(db.Integer(),db.ForeignKey('usertype.id'))
    
    #other fields
    creation_date = db.Column(db.Date(),nullable=False)
    write_date =  db.Column(db.Date(),nullable=False)
    

    
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
    
    #other fields
    user_uid = db.Column(db.Integer(),db.ForeignKey('users.id'))
    
    create_uid = db.Column(db.Integer())
    write_uid = db.Column(db.Integer())
    creation_date = db.Column(db.Date(),nullable=False)
    write_date =  db.Column(db.Date(),nullable=False)
    

    