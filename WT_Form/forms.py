from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms import validators, ValidationError

class StudentForm(FlaskForm):
    name = StringField("Student Name", [validators.DataRequired("Please enter your name")])
    marks = IntegerField("Marks", [validators.DataRequired("Please enter your marks")])
    email = StringField("Email", [validators.DataRequired("Please enter your email"), validators.Email("Invalid email address")])

    submit = SubmitField("Submit")