from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp

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