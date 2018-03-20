from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, RadioField, TextAreaField, HiddenField, BooleanField
from wtforms.validators import DataRequired, Email

#All the forms used for the website


class LoginForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired("Please Enter Your Email"),Email("Please Enter a Valid Email")])
    password = PasswordField("Password", validators=[DataRequired("Please Enter a Password")])
    user = RadioField("User Type:",choices=[("Mentor","I am a Mentor"),("Mentee","I am a Mentee")])
    submit = SubmitField("Login")

class Admin(FlaskForm):
    username = StringField("Username", validators=[DataRequired("Please Enter Your Username")])
    password = PasswordField("Password",validators=[DataRequired("Please enter your password")])
    submit = SubmitField("Login")

class AddSite(FlaskForm):
    name = StringField("Student Name")
    url = StringField("Student's site with https:// included")
    titletag = StringField("What is the tag used to identify blog titles")
    titleclass = StringField("What class or attribute does the title tag have?")
    bodytag = StringField("What tag is used for the content of the blog?")
    bodyclass = StringField("What class or attribute does the body tag have?")
    submit = SubmitField("Add Site")

class DeleteSite(FlaskForm):
    studentName = HiddenField()
    submit = SubmitField("Remove Site")
