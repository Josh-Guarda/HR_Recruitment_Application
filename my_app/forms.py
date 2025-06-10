from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired,ValidationError
from my_app.models import Users


class RegisterForm(FlaskForm):
    
    def validate_username(self, username_to_check):
        user = Users.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('UserName Already exist! Please try different UserName.')
        
    def validate_email_address(self, email_address_to_check):
        email_address = Users.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Already exist! Please try a different Email Address.')
    
    username = StringField(label='User Name', validators=[Length(min=6,max=30), DataRequired()])
    username = StringField(label='User Name', validators=[Length(min=6,max=30), DataRequired()])
    email_address=StringField(label='Email Address', validators=[Email(), DataRequired()])
    password1= PasswordField(label='Password' , validators=[Length(min=8,max=30), DataRequired()])
    password2= PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()])
    submit=SubmitField(label='Create Account')
    
    

class LoginForm(FlaskForm):
    username = StringField(label='User Name', validators= [DataRequired()]) 
    password1= PasswordField(label='Password' , validators=[DataRequired()])
    submit=SubmitField(label='Sign in')
    
    
