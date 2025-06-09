from my_app import db





class UserType(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(length=30),unique=True,nullable=False)
    
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
    
    department_id=db.relationship('Item',backref='owned_user',lazy=True)
    manager_id= db.Column(db.Integer(),unique=True)
    user_type=db.Column(db.String(length=15),nullable=False)
    
    create_uid = db.Column(db.Integer())
    write_uid = db.Column(db.Integer())
    creation_date = db.Column(db.Date(),nullable=False)
    write_date =  db.Column(db.Date(),nullable=False)
    
    
class department(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(length=30),nullable=False)
    manager_id= db.Column(db.Integer(),unique=True)
    
    create_uid = db.Column(db.Integer())
    write_uid = db.Column(db.Integer())
    creation_date = db.Column(db.Date(),nullable=False)
    write_date =  db.Column(db.Date(),nullable=False)
    
    
class Jobs(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    job_title=db.Column(db.String(length=30),nullable=False)
    department_id = db.Column(db.Integer())
    
    department =db.Column(db.String(length=30),nullable=False)
    employment_type=db.Column(db.String(length=15),nullable=False)
    min_sal= db.Column(db.Float(),nullable=False)
    max_sal= db.Column(db.Float(),nullable=False)
    start_date = db.Column(db.Date(),nullable=False)
    location =db.Column(db.String(length=50),nullable=False)
    description =db.Column(db.String(length = 1030), nullable=False, unique=True)
    start_date = db.Column(db.Date(),nullable=False)
    
    create_uid = db.Column(db.Integer())
    write_uid = db.Column(db.Integer())
    creation_date = db.Column(db.Date(),nullable=False)
    write_date =  db.Column(db.Date(),nullable=False)
    

    