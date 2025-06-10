from my_app import db



class UserType(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(length=30),unique=True,nullable=False)
    
    user_type=db.relationship('User',backref='user_type',lazy=True)
 
 
 
class Department(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(length=30),nullable=False)
    manager_id= db.Column(db.Integer(),unique=True)
    
    department_jobs_id = db.relationship('Jobs',backref='dept_name_jobs',lazy=True)
    department_user_id = db.relationship('Users',backref='dept_name_users',lazy=True)
    
    #other fields
    create_uid = db.Column(db.Integer(),db.ForeignKey('users.id'))
    write_uid = db.Column(db.Integer(),db.ForeignKey('users.id'))
    
    creation_date = db.Column(db.Date(),nullable=False)
    write_date =  db.Column(db.Date(),nullable=False)
    
 
 
class Users(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(length=30),unique=True,nullable=False)
    password_hash=db.Column(db.String(length=30),nullable=False)
    email_address=db.Column(db.String(length=50),nullable=False,unique=True)
    department =db.Column(db.String(length=30),nullable=False)
    
    
    department_id =db.Column(db.Integer, db.ForeignKey('department.id'))
    user_type_id = db.Column(db.Integer, db.ForeignKey('user_type.id'))
    
    rel_create_id_jobs = db.relationship('Jobs',backref='creator_id_jobs',lazy=True)
    rel_write_id_jobs = db.relationship('Jobs',backref='writer_id_jobs',lazy=True)
    rel_create_id_dept = db.relationship('Department',backref='creator_id_dept',lazy=True)
    rel_write_id_dept = db.relationship('Department',backref='writer_id_dept',lazy=True)
    
    
    
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
    create_uid = db.Column(db.Integer(),db.ForeignKey('users.id'))
    write_uid = db.Column(db.Integer(),db.ForeignKey('users.id'))
    creation_date = db.Column(db.Date(),nullable=False)
    write_date =  db.Column(db.Date(),nullable=False)
    

    