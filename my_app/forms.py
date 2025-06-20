from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,HiddenField
from wtforms.validators import Length, EqualTo, Email, DataRequired,ValidationError
from my_app.models import Users,Usertype


class RegisterForm(FlaskForm):
    
    def validate_username(self, username_to_check):
        user = Users.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('UserName Already exist! Please try different UserName.')
        
    def validate_email_address(self, email_address_to_check):
        email_address = Users.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Already exist! Please try a different Email Address.')
    
    firstname = StringField(label='First Name', validators=[Length(min=6,max=30), DataRequired()])
    lastname = StringField(label='Last Name', validators=[Length(min=6,max=30), DataRequired()])
    email_address=StringField(label='Email', validators=[Email(), DataRequired()])
    password= PasswordField(label='Password' , validators=[Length(min=3,max=30), DataRequired()])
    password2= PasswordField(label='Confirm Password', validators=[EqualTo('password'), DataRequired()])
    usertype = HiddenField(label='User Type')
    
    submit=SubmitField(label='Create Account')
    
    

class LoginForm(FlaskForm):
    email_address = StringField(label='Email', validators= [DataRequired()]) 
    password= PasswordField(label='Password' , validators=[DataRequired()])
    submit=SubmitField(label='Sign in')
    
    

# class Personal_info(FlaskForm):
    
    