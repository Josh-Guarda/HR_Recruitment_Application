from my_app import app,db
from my_app import BARANGAY_DATA, MUNICIPALITY_DATA, PROVINCE_DATA
from my_app import  MUNICIPALITY_DATA, PROVINCE_DATA,mail,Message,generate_reset_token,verify_reset_token
from flask import render_template, redirect, url_for, flash,request,session
from my_app.models import Jobs,Users
from my_app.forms import RegisterForm,LoginForm,PersonalInfoForm,PasswordResetRequest,ResetPasswordForm,ChangePasswordForm
from flask_login import login_user,current_user,logout_user,login_required
from datetime import datetime
from werkzeug.utils import secure_filename
import uuid
import os




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



# # ✅ Forgot Password Route
# @app.route('/forgot-password', methods=['POST'])
# def forgot_password():
#     reset_pw_request=PasswordResetRequest()
#     if reset_pw_request.validate_on_submit():
#         email_address = reset_pw_request.email_address.data
#         if email_address:
#             print("Email fetched: ",email_address) #console check ✅
    
#     try:
#         # Generate Reset Token
#         token = generate_reset_token(email_address)
#         reset_link = url_for('reset_password', token=token, _external=True)

#         # Send Email
#         msg = Message('Password Reset Request', sender='noreply@wakenbake.com', recipients=[email_address])
#         msg.body = f'Click the link to reset your password: {reset_link}'
#         mail.send(msg)

#         flash('Password reset link has been sent to your email!', 'success')
#     except Exception as e:
#         print(e)
#         flash('An error occurred while sending email. Please try again.', 'error')

#     return redirect(url_for('login'))  # Redirect to login page after sending email


# ✅ Reset Password Route
# @app.route('/reset-password/<token>', methods=['GET', 'POST'])
# def reset_password(token):
#     reset_pw_form= ResetPasswordForm()
#     email = verify_reset_token(token)
#     if not email:
#         flash('Invalid or expired token', 'error')
#         return redirect(url_for('login'))

#     if reset_pw_form.validate_on_submit():
#         new_password = reset_pw_form.password.data
#         confirm_password = reset_pw_form.password2.data

#         if new_password != confirm_password:
#             flash('Passwords do not match!', 'error')
#             return redirect(url_for('reset_password', token=token))


#         # Update password in the database
#         db.session.commit()
#         flash('Your password has been updated!', 'success')
#         return redirect(url_for('public_dashboard'))

#     return render_template('reset_password.html', token=token)  # ✅ Pass token to template


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
@login_required
def internal_dashboard():
    if current_user.user_type.name != "internal":
        return redirect(url_for("home_page"))
    return render_template('internal/internal_dashboard.html',show_navbar=False)


@app.route('/public/', methods=["GET", "POST"])
@login_required
def public_dashboard():
    form = PersonalInfoForm(obj=current_user)
    pwr_form = PasswordResetRequest()
    change_pw_form= ChangePasswordForm()
    
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
    
    
    
    
    # Submit HANDLERS
    
    # Change Password Request HANDLER
    if change_pw_form.submit.data and change_pw_form.validate_on_submit():
        # if change_pw_form.current_password.data != current_user.password:
        if not current_user.check_password_correction(change_pw_form.current_password.data):
            flash('Password is Incorrect', category='danger')
            
        else:
            new_password = change_pw_form.password.data
            confirm_password = change_pw_form.password2.data

            if new_password != confirm_password:
                flash('New passwords do not match with Confirm Password!',category='danger')
                
            else:
                flash(f'Password changed Successfully!', category='success')
                current_user.password = new_password
                db.session.commit()
                return redirect(url_for('public_dashboard'))

    if change_pw_form.errors:
        for err_msg in change_pw_form.errors.values():
            flash(f'Error: {err_msg}', category='danger')
    
    
    # # Password Reset Request HANDLER
    # if pwr_form.submit.data and pwr_form.validate_on_submit():
    #     input_email_address=pwr_form.email_address.data
        
    #     # Your password reset email logic here
    #     # send_reset_email(pwr_form.email_address.data)  
        
    #     flash('Password reset email sent!', 'primary')
    #     return redirect(url_for('public_dashboard'))
    
    # if pwr_form.errors:
    #     for err_msg in pwr_form.errors.values():
    #         flash(f'Error: {err_msg}', category='danger')
    
    
    
    # Personal Information UPDATE HANDLER
    if form.update.data and form.validate_on_submit():
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

    return render_template('public/public_dashboard.html', show_navbar=False, form=form, pwr_form=pwr_form, change_pw_form=change_pw_form)



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



# @app.route('/profile-settings')
# @login_required
# def profile_settings():
#     if current_user.user_type.name != "public":
#         return redirect(url_for("home_page"))
#     return render_template('public/profile_settings.html')


@app.route('/logout')
def logout_page():
    logout_user()
    session.clear()  # Clear all session data
    flash('You have been logged out!"', category= 'primary')
    return redirect(url_for('home_page'))











