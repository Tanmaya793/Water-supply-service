from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, DateField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp, Optional, EqualTo

class Contact(FlaskForm):

    fullname = StringField(
        "Full Name",
        validators = [DataRequired(), Length(3,20)]
    )

    email = StringField(
        "Email",
        validators = [DataRequired(), Email()]
    )

    mobile = StringField(
        'Mobile Number', 
        validators = [DataRequired(), Regexp(r'^[6-9]\d{9}$', message="Enter a valid 10-digit mobile number starting with 6-9")
    ])

    message = TextAreaField(
        "message"
    )

    submit = SubmitField(
        "Submit"
    )

class SignupForm(FlaskForm):
    
    username = StringField(
        "Username",
        validators = [DataRequired(), Length(4,15)]
    )

    email = StringField(
        "Email",
        validators = [DataRequired(), Email()]
    )

    gender = SelectField(
        "Gender",
        choices = ["male","female","others"],
        validators = [Optional()]
    )

    dob = DateField(
        "Date of Birth",
        validators = [DataRequired()]
    )

    password = PasswordField(
        "Password",
        validators = [DataRequired(), Length(5,15)]
    )

    confirmPassword = PasswordField(
        "ConfirmPassword",
        validators = [DataRequired(), Length(5,15), EqualTo("password")]
    )

    submit = SubmitField(
        "Submit"
    )

class LoginForm(FlaskForm):

    email = StringField(
        "Email",
        validators = [DataRequired(), Email()]
    )

    password = PasswordField(
        "Password",
        validators = [DataRequired(), Length(5,15)]
    )

    remeberme = BooleanField(
        "Remember Me"
    )

    submit = SubmitField(
        "Log in"
    )