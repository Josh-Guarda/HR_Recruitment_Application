from my_app import app,db
from my_app import BARANGAY_DATA, MUNICIPALITY_DATA, PROVINCE_DATA
from my_app import mail,Message,generate_reset_token,verify_reset_token
# from my_app.helper import set_form_province,set_form_municipality,set_form_barangay
from my_app.helper import set_form_choices
from flask import render_template, redirect, url_for, flash,request,session, jsonify
from my_app.models import Jobs,Users,Usertype
from my_app.forms import RegisterForm,LoginForm,PersonalInfoForm,ChangePasswordFormInSecurity,ForgotPassword,ChangePasswordBeforeLogin
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



# ✅ Forgot Password Route
@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password_page():
    forgot_pw_request=ForgotPassword()
    if forgot_pw_request.validate_on_submit():
        email_address = forgot_pw_request.email_address.data
        if email_address:
            print("Email fetched: ",email_address)
    
        try:
            # Generate Reset Token
            token = generate_reset_token(email_address)
            reset_link = url_for('change_password_page', token=token, _external=True)

            # Send Email
            msg = Message('Password Reset Request', sender='noreply@wakenbake.com', recipients=[email_address])
            msg.body = f'Click the link to reset your password: {reset_link}'
            mail.send(msg)

            flash('Password reset link has been sent to your email!', 'success')
        except Exception as e:
            print(e)
            flash('An error occurred while sending email. Please try again.', 'error')

        return redirect(url_for('login_page'))  # Redirect to login page after sending email
    

    return render_template('auth/password_reset_request.html',forgot_pw_request=forgot_pw_request)
    # return render_template('auth/password_reset_request.html', token=token)  # ✅ Pass token to template



@app.route('/change-password/<token>', methods=['GET', 'POST'])
def change_password_page(token):
    change_pw_form= ChangePasswordBeforeLogin()
    email = verify_reset_token(token)
    # print(f'your email: {email}')
    if not email:
        flash('Invalid or expired token',category='danger')
        return redirect(url_for('login_page'))

    if change_pw_form.validate_on_submit():
        # print('TEST')
        new_password = change_pw_form.password.data
        confirm_password = change_pw_form.password2.data

        if new_password != confirm_password:
            flash('New passwords do not match with Confirm Password!', category='danger')
            return redirect(url_for('change_password_page', token=token, change_pw_form=change_pw_form))

        
        # Update password in the database
        else:
            user_to_change_pw = Users.query.filter_by(email_address=email).first()
            user_to_change_pw.password = new_password
            db.session.commit()

            flash('Your password has been updated!', 'success')
            return redirect(url_for('public_dashboard'))
    
    return render_template('auth/change_password.html', token=token,change_pw_form=change_pw_form)




@app.route("/login",methods=["GET","POST"])
def login_page(): 
    form=LoginForm()
    if form.validate_on_submit():
        attempted_user = Users.query.filter_by(email_address=form.email_address.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.firstname}', category='success')
            
            if current_user.user_type.name == 'admin':
                return redirect(url_for('admin_dashboard'))
            elif current_user.user_type.name == 'internal':
                return redirect(url_for('internal_dashboard'))
            else:
                return redirect(url_for('career_page'))
        else:
            flash('Invalid username or password.', category='danger')
            
    
    return render_template('auth/login.html',show_navbar=False,form=form)




# ADMIN ROUTES
@app.route('/admin-dashboard/')
@login_required
def admin_dashboard():
    if current_user.user_type.name != "admin":
        return redirect(url_for("home_page"))
    return render_template("admin/admin_dashboard.html",show_navbar=False)



@app.route('/admin-get-users/', methods=["GET"])
@login_required
def admin_dashboard_manage_users():
    users = Users.query.all()
    # No need to create forms here anymore since Edit template is dynamically loaded via User Modal handle via JS.
    return render_template('admin/admin_users_management.html', users=users)



@app.route('/get-user-form/<int:user_id>', methods=["GET"])
@login_required
def get_user_form(user_id):
    user = Users.query.get_or_404(user_id)
    user_data = {
                "id": user.id,
                "profile_picture": user.profile_picture,
                "firstname": user.firstname,
                "lastname": user.lastname,
                "address_1": user.address_1,
                "address_2": user.address_2,
                "zipcode": user.zipcode,
                "email_address": user.email_address,
                "mobile_number": user.mobile_number,
                "phone_number": user.phone_number,
                "prov_id": user.prov_id,
                "munci_id": user.munci_id,
                "brgy_id": user.brgy_id,
                "user_type":user.user_type_id
                }
    return jsonify(user_data)
    # return user_id


@app.route('/update-user-form/<int:user_id>', methods=["POST"])
@login_required
def update_user_form(user_id):
    user = Users.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    
    
    
    original_user_type = user.user_type_id
    current_user_updating_self = (user.id == current_user.id)
    
    

    
    if request.method == "POST":
        # Handle form fields (non-file)
        for k, v in request.form.items():
            print({k: v})
            
            if k == 'user_type':
                # Convert to integer and get the actual Usertype object
                user_type_id = int(v)
                user_type_obj = Usertype.query.get(user_type_id)
                if user_type_obj:
                    user.user_type = user_type_obj  # Set the relationship object
                else:
                    print(f"Warning: UserType ID {user_type_id} not found")
            # Handle other fields normally
            elif hasattr(user, k):
                setattr(user, k, v)

        # Handle file upload (your existing code)
        if 'profile_picture' in request.files:
            avatar_file = request.files['profile_picture']
            if avatar_file.filename != '':
                filename = secure_filename(avatar_file.filename)
                avatar_name = str(uuid.uuid4()) + "_" + filename
                upload_path = os.path.join(app.config['UPLOAD_FOLDER'], avatar_name)
                avatar_file.save(upload_path)
                user.profile_picture = avatar_name

        db.session.commit()
        
        #handles Automatically logs out the current_user if he updates his/her user_type_id
        #note: that this feature is only available in ADMIN access:
        if current_user_updating_self and user.user_type_id != original_user_type:
            return jsonify({
                    "success": True,
                    "message": "User updated successfully",
                    "toast": {
                        "message": "Profile updated! Please login again with your new role.",
                        "category": "success"
                    },
                    "redirect": url_for('logout_page')
                })
        else:
            return jsonify({
                "success": True,
                "message": "User updated successfully",
                "toast": {
                    "message": f"{user.firstname}'s profile has been updated!",
                    "category": "success"
                }
            })
        

        
    


# Internal ROUTES
@app.route('/internal-dashboard/')
@login_required
def internal_dashboard():
    if current_user.user_type.name != "internal":
        return redirect(url_for("home_page"))
    return render_template('internal/internal_dashboard.html',show_navbar=False)





# Public ROUTES
@app.route('/public/<int:user_id>', methods=["GET", "POST"])
@login_required
def public_dashboard(user_id):
    form = PersonalInfoForm(obj=current_user)
    change_pw_form= ChangePasswordFormInSecurity()

    if request.method == 'GET':
        # Pre-populate form with user data
        if current_user:
            form.firstname.data = current_user.firstname
            form.lastname.data = current_user.lastname
            form.address_1.data = current_user.address_1
            form.address_2.data = current_user.address_2
            form.zipcode.data = current_user.zipcode
            form.email_address.data = current_user.email_address
            form.mobile_number.data = current_user.mobile_number
            form.phone_number.data = current_user.phone_number
            
            # Set the selected values for dropdowns
            
            form.prov_id.data = str(current_user.prov_id) if current_user.prov_id else ''
            form.munci_id.data = str(current_user.munci_id) if current_user.munci_id else ''
            form.brgy_id.data = str(current_user.brgy_id) if current_user.brgy_id else ''
            set_form_choices(form, current_user)
            
        
    else:
        set_form_choices(form, current_user)
        
        
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




    # Personal Information UPDATE HANDLER
    if form.update.data and form.validate_on_submit():
    # if request.method=="POST":    
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

        
        # print(f"Form values - prov: {form.prov_id.data}, munci: {form.munci_id.data}, brgy: {form.brgy_id.data}")
        # print(f"Type of prov_id: {type(form.prov_id.data)}")
        # print(f"After save - prov: {current_user.prov_id}, munci: {current_user.munci_id}, brgy: {current_user.brgy_id}")
        db.session.commit()
        flash('Your profile has been updated!', category='success')
        
        return redirect(url_for('public_dashboard',user_id=current_user.id))
    
    if form.cancel.data:
            flash('Update Canceled.', category='danger')
            return redirect(url_for('public_dashboard',user_id=current_user.id))

    if form.errors:
        for err_msg in form.errors.values():
            flash(f'Error encounter in {form}: {err_msg}', category='danger')

    if current_user.user_type.name != "public":
        return redirect(url_for("home_page"))

    return render_template('public/public_dashboard.html', show_navbar=False, form=form, change_pw_form=change_pw_form)






@app.route('/get_user_types', methods=["GET"])
def get_user_type():
    types = Usertype.query.all()
    list_types = []
    for type in types:
        user_type = {
            "id" : type.id,
            "name": type.name
        }
        list_types.append(user_type)
        
    # print(f"USER_TYPES FOUND{type}")
    
    return jsonify(list_types)


@app.route('/get_provinces')
def get_provinces():
    provinces = sorted(
        [{"code": str(m['provCode']), "name": m['provDesc']} 
         for m in PROVINCE_DATA],
        key=lambda x: x['name'].lower()
    )
    
    # print(f"Generated Provinces{provinces}")
    return jsonify(provinces)


@app.route('/get_municipalities/<prov_code>')
def get_municipalities(prov_code):
    municipalities = sorted(
        [{"code": str(m['citymunCode']), "name": m['citymunDesc']} 
         for m in MUNICIPALITY_DATA if str(m['provCode']) == prov_code],
        key=lambda x: x['name'].lower()
    )
    return jsonify(municipalities)

@app.route('/get_barangays/<munci_code>')
def get_barangays(munci_code):
    barangays = sorted(
        [{"code": str(b['brgyCode']), "name": b['brgyDesc']} 
         for b in BARANGAY_DATA if str(b['citymunCode']) == munci_code],
        key=lambda x: x['name'].lower()
    )
    return jsonify(barangays)






@app.route('/logout')
def logout_page():
    logout_user()
    session.clear()  # Clear all session data
    flash('You have been logged out!"', category= 'primary')
    return redirect(url_for('home_page'))



