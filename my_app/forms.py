from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,HiddenField,SelectField,SearchField
from flask_login import current_user
from wtforms.validators import Length, EqualTo, Email, DataRequired,ValidationError
from my_app.models import Users,Usertype
from flask_wtf.file import FileField,FileAllowed


### Login and Authentication Forms ##
# Main User Registration
class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = Users.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('UserName Already exist! Please try different UserName.')
        
    def validate_email_address(self, email_address_to_check):
        email_address = Users.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Already exist! Please try a different Email Address.')
    
    firstname = StringField(label='First Name', validators=[Length(min=3,max=30), DataRequired()])
    lastname = StringField(label='Last Name', validators=[Length(min=3,max=30), DataRequired()])
    email_address=StringField(label='Email', validators=[Email(), DataRequired()])
    password= PasswordField(label='Password' , validators=[Length(min=3,max=30), DataRequired()])
    password2= PasswordField(label='Confirm Password', validators=[EqualTo('password'), DataRequired()])
    usertype = HiddenField(label='User Type')
    
    submit=SubmitField(label='Create Account')
    
# main Login Form
class LoginForm(FlaskForm):
    email_address = StringField(label='Email', validators= [DataRequired()]) 
    password= PasswordField(label='Password' , validators=[DataRequired()])
    submit=SubmitField(label='Sign in')
    
# Forgot request form
class ForgotPassword(FlaskForm):
    email_address=StringField(label='Email Address', validators=[Email(),DataRequired()])
    submit=SubmitField(label='Reset Password')
    
# Change Password trigger in Login Form
class ChangePasswordBeforeLogin(FlaskForm):
    password= PasswordField(label=' New Password' , validators=[Length(min=3,max=30), DataRequired()])
    password2= PasswordField(label='Confirm Password',validators=[ DataRequired()])
    submit=SubmitField(label='Change Password')
    
    







### Dashboard / Admin,Internal Dashboard Landing Route ###

# class UsersManagement(FlaskForm):
    



















### Personal Information Form / Public Dashboard Landing Route ###
class PersonalInfoForm(FlaskForm):
    def validate_mobile_number(self, number_to_check):
        if not number_to_check.data.isdigit():
            raise ValidationError('Only numbers are allowed.')

        number_to_save = Users.query.filter_by(mobile_number=number_to_check.data).first()
        if number_to_save and number_to_save.id !=current_user.id:
            raise ValidationError('Mobile number already exists.')
        
    def validate_phone_number(self, number_to_check):
        if not number_to_check.data.isdigit():
            raise ValidationError('Only numbers are allowed.')

        number_to_save = Users.query.filter_by(phone_number=number_to_check.data).first()
        if number_to_save and number_to_save.id !=current_user.id:
            raise ValidationError('Phone number already exists.')
        
    avatar= FileField('image', validators=[FileAllowed(['jpg','jpeg','png'], 'Images only!')])
    firstname = StringField(label='First Name', validators=[Length(min=3,max=30), DataRequired()])
    lastname = StringField(label='Last Name', validators=[Length(min=3,max=30), DataRequired()])
    address_1 =  StringField(label='Address 1', validators=[Length(min=6,max=50)])
    address_2 =  StringField(label='Address 2', validators=[Length(min=6,max=50)])
    
    brgy_id =  SelectField(label='Barangay')
    munci_id =  SelectField(label='Municipality')
    prov_id =  SelectField(label='Province')
    zipcode = StringField(label='ZipCode', validators=[Length(min=4,max=4)])
    
    email_address=StringField(label='Email', validators=[Email(), DataRequired()])
    mobile_number = StringField(label='Mobile Number', validators=[Length(min=11,max=11), DataRequired()])
    phone_number=StringField(label='Landline Number', validators=[Length(min=8,max=8)],default=('00000000'))
    
    update=SubmitField(label='Save',name='update_profile')
    cancel=SubmitField(label='Cancel')
    
    
# Change Password trigger in Security Nav inside Employee Profile
class ChangePasswordFormInSecurity(FlaskForm):
    current_password = PasswordField(label='Password' , validators=[Length(min=3,max=30), DataRequired()])
    password= PasswordField(label='New Password' , validators=[Length(min=3,max=30), DataRequired()])
    password2= PasswordField(label='Confirm Password',validators=[ DataRequired()])
    submit=SubmitField(label='Update Password')
    


