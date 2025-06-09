from my_app import app
from flask import render_template,url_for
from my_app.models import Jobs

@app.route("/")
@app.route("/home")

def home_page():
    return render_template('main.html')
    

@app.route("/career")
def career_page():
    jobs=Jobs.query.all()
    
    
    
    
    # jobs= [
    #     {'id':1,'job_title':'Sr. Software Engineer','department':'Information Technology','employment_type':'Full-time','min_sal':80000,'max_sal':100000,'start_date':'07/01/2025','location':'Bonifacio Global City Taguig','description':'We are looking for an experienced software developer to join our team. You will be responsible for developing high-quality applications and working with the latest technologies.'},
    #     {'id':2,'job_title':'Sr. Marketing Manager','department':'Marketing Department','employment_type':'Full-time','min_sal':80000,'max_sal':100000,'start_date':'07/01/2025',
    #      'location':'Manila','description':'We are looking for an experienced Marketing Manager to join our team. You will be responsible on managing Planning and Resources Management.'},       
    #     {'id':3,'job_title':'Hr Recruitment Manager','department':'Human Resources','employment_type':'Part-time','min_sal':50000,'max_sal':60000,'start_date':'07/01/2025',
    #      'location':'Makati City','description':'We are looking for an experienced Recruitment Manager to join our team. You will be responsible on HumanResources Management and Recruitment.'}
    # ]
    # ,job=job
    return render_template("career.html",jobs=jobs)






@app.route("/register")
def register_page():
    return render_template('register.html')


@app.route("/login")
def login_page():
    return render_template('login.html')