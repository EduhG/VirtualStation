from flask_wtf import Form
from wtforms import SubmitField, validators, PasswordField, StringField, BooleanField


class SigninForm(Form):
    email = StringField("Email", [validators.DataRequired("Please enter your login email.")])
    password = PasswordField('Password', [validators.DataRequired("Please enter a password.")])
    remember_me = BooleanField('remember_me', default=False)

    submit = SubmitField("Sign In")
