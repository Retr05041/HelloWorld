# This is where we will be creating our forms

from flask_wtf import FlaskForm # from flask_wtf import the class we need
from wtforms import StringField, PasswordField, SubmitField, BooleanField # gets string input | and pass input
from wtforms.validators import DataRequired, Length, Email, EqualTo # imports validators

# CLASS FOR REGISTRATION FORM - INHERANTS FROM "FlaskForm"
# REGISTRATION FORM
class RegistrationForm(FlaskForm):

    # makes an username input with the label "username" | with validators to make sure data is inputed and that it is not longer than 20 
    username = StringField("Username", validators=[DataRequired(), Length(min=1, max=20)]) 

    email = StringField("Email", validators=[DataRequired(), Email()]) # makes sure email is an email

    password = PasswordField("Password", validators=[DataRequired()]) # input pass
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")]) # confirm pass | makes sure its equal to password

    submit = SubmitField("Sign Up")


# LOGIN FORM
class LoginForm(FlaskForm):

    email = StringField("Email", validators=[DataRequired(), Email()])

    password = PasswordField("Password", validators=[DataRequired()])

    remember = BooleanField("Remember Me") # remember me as a true or false

    submit = SubmitField("Login") # duh


