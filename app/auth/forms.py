from flask_wtf import Form
from wtforms import SubmitField, validators, PasswordField, StringField, BooleanField


class SigninForm(Form):
    email = StringField("Email", [validators.DataRequired("Please enter your login email.")])
    password = PasswordField('Password', [validators.DataRequired("Please enter a password.")])
    remember_me = BooleanField('remember_me', default=False)

    submit = SubmitField("Sign In")


class SignupForm(Form):
    first_name = StringField('First Name', [validators.DataRequired("Please enter your user name.")])
    other_names = StringField('Other Names', [validators.DataRequired("Please enter your user name.")])
    email = StringField("Email", [validators.DataRequired("Please enter your email address."),
                        validators.Email("Please enter your email address.")])
    username = StringField('User Name', [validators.DataRequired("Please enter your user name.")])
    password = PasswordField('Password', [validators.DataRequired("Please enter a password.")])
    password_again = PasswordField('Confirm Password', [validators.DataRequired("Please enter a password.")])

    submit = SubmitField("Create Account")
