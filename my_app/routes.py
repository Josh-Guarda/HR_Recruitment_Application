from my_app import app,db
# from my_app import Barangay_JSON
# from flask import jsonify

from my_app import BARANGAY_DATA, MUNICIPALITY_DATA, PROVINCE_DATA
from my_app import  MUNICIPALITY_DATA, PROVINCE_DATA

from flask import render_template, redirect, url_for, flash,request
from my_app.models import Jobs,Users,Usertype
from my_app.forms import RegisterForm,LoginForm,PersonalInfoForm,ValidationError
from flask_login import login_user,current_user, logout_user, login_required
from datetime import datetime
from werkzeug.utils import secure_filename
import uuid
import os
import json





@app.route("/")
@app.route("/home")
def home_page():
    return render_template('main.html',show_navbar=True)
    

@app.route("/career")
@login_required
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
    return render_template("career.html",jobs=jobs,show_navbar=True)






@app.route("/register",methods=['GET','POST'])
def register_page():
    
    # TOdo:: Create a separate Create user Interface or Modal that has an option of a usertype for Admin Access. this will serves as dynamic creation of User if 
    # the user of the app define an internal User
    
    
    

    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = Users(firstname=form.firstname.data,
                               lastname=form.lastname.data,
                               email_address=form.email_address.data,
                               password=form.password.data,  #instead of using password_has the password_hash declare in models.py is undergone to some conversion for encryption using flask_bcrypt see Users Model
                               user_type_id = 3, #hard Coded user_type_id to set as PUBLIC USER(3) for all users register to website
                               creation_date = datetime.now().date(),
                               write_date = datetime.now().date()
                               )

        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Account create successfully! You are now logged in as {user_to_create.firstname}',category='success')
        return redirect(url_for('career_page'))
        

    if form.errors !={}: # if there is no errors from validations inside the forms.py
        for err_msg in form.errors.values():
            flash(f'There is some Error in {err_msg}',category='danger')

    return render_template('auth/register.html',show_navbar=False,form=form)




@app.route("/login",methods=["GET","POST"])
def login_page(): 
    form=LoginForm()
    if form.validate_on_submit():
        attempted_user = Users.query.filter_by(email_address=form.email_address.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.firstname}', category='success')
            return redirect(url_for('career_page'))
        else:
            flash('Invalid username or password.', category='danger')
    
    return render_template('auth/login.html',show_navbar=False,form=form)




@app.route('/admin/')
@login_required
def admin_dashboard():
    if current_user.user_type.name != "admin":
        return redirect(url_for("home_page"))
    return render_template("admin/admin_dashboard.html",show_navbar=False)
    
@app.route('/internal/') 
def internal_dashboard():
    if current_user.user_type.name != "internal":
        return redirect(url_for("home_page"))
    return render_template('internal/internal_dashboard.html',show_navbar=False)



@app.route('/public/', methods=["GET", "POST"])
@login_required
def public_dashboard():
    form = PersonalInfoForm(obj=current_user)

    # Province always preloaded
    form.prov_id.choices = [('', '-- Select Province --')] + sorted(
        [(prov['provCode'], prov['provDesc']) for prov in PROVINCE_DATA],
        key=lambda x: x[1].lower()
    )

    # Only set muni/brgy choices if form has values or user has saved data
    selected_prov = form.prov_id.data or current_user.prov_id
    selected_muni = form.munci_id.data or current_user.munci_id

    if selected_prov:
        form.munci_id.choices = [('', '-- Select Municipality --')] + sorted(
            [(m['citymunCode'], m['citymunDesc']) for m in MUNICIPALITY_DATA if m['provCode'] == selected_prov],
            key=lambda x: x[1].lower()
        )
    else:
        form.munci_id.choices = [('', '-- Select Municipality --')]

    if selected_muni:
        form.brgy_id.choices = [('', '-- Select Barangay --')] + sorted(
            [(b['brgyCode'], b['brgyDesc']) for b in BARANGAY_DATA if b['citymunCode'] == selected_muni],
            key=lambda x: x[1].lower()
        )
    else:
        form.brgy_id.choices = [('', '-- Select Barangay --')]

    # Submit handler
    if form.validate_on_submit():
        if form.cancel.data:
            flash('Update Canceled.', category='danger')
            return redirect(url_for('public_dashboard'))

        current_user.firstname = form.firstname.data
        current_user.lastname = form.lastname.data
        current_user.email_address = form.email_address.data
        current_user.mobile_number = form.mobile_number.data
        current_user.phone_number = form.phone_number.data
        current_user.address_1 = form.address_1.data
        current_user.address_2 = form.address_2.data
        current_user.prov_id = form.prov_id.data
        current_user.munci_id = form.munci_id.data
        current_user.brgy_id = form.brgy_id.data
        current_user.zipcode = form.zipcode.data

        # Avatar logic
        if form.avatar.data:
            avatar_file = form.avatar.data
            filename = secure_filename(avatar_file.filename)
            avatar_name = str(uuid.uuid4()) + "_" + filename
            upload_path = os.path.join(app.config['UPLOAD_FOLDER'], avatar_name)
            try:
                avatar_file.save(upload_path)
                current_user.profile_picture = avatar_name
            except FileNotFoundError:
                flash('Avatar upload directory not found!', category='danger')

        db.session.commit()
        flash('Your profile has been updated!', category='success')
        return redirect(url_for('public_dashboard'))

    if form.errors:
        for err_msg in form.errors.values():
            flash(f'Error: {err_msg}', category='danger')

    if current_user.user_type.name != "public":
        return redirect(url_for("home_page"))

    return render_template('public/public_dashboard.html', show_navbar=False, form=form)



@app.route('/get_municipalities')
def get_municipalities():
    prov_code = request.args.get('prov_code')
    results = [
        {'code': muni['citymunCode'], 'name': muni['citymunDesc']}
        for muni in MUNICIPALITY_DATA if muni['provCode'] == prov_code
    ]
    return {'data': results}


@app.route('/get_barangays')
def get_barangays():
    muni_code = request.args.get('muni_code')
    results = [
        {'code': brgy['brgyCode'], 'name': brgy['brgyDesc']}
        for brgy in BARANGAY_DATA if brgy['citymunCode'] == muni_code
    ]
    return {'data': results}




@app.route('/logout')
def logout_page():
    logout_user()
    flash('You have been logged out!"', category= 'primary')
    return redirect(url_for('home_page'))











