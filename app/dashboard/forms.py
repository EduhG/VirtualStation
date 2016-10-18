from flask_wtf import Form
from wtforms import SubmitField, validators, StringField, RadioField, TextAreaField, SelectField


class NewCaseForm(Form):
    id_method = StringField("Email", [validators.DataRequired("Please enter your login email.")])
    id_number = StringField("Email", [validators.DataRequired("Please enter your login email.")])
    first_name = StringField("Email", [validators.DataRequired("Please enter your login email.")])
    other_names = StringField("Email", [validators.DataRequired("Please enter your login email.")])
    gender = RadioField('Gender', choices=[('Male', 'Male'),
                                           ('Female', 'Female')])
    phone_number = StringField("Email", [validators.DataRequired("Please enter your login email.")])
    email = StringField("Email", [validators.DataRequired("Please enter your login email.")])
    # reg_date
    description = TextAreaField('Description', [validators.DataRequired("Please enter your login email.")])

    submit = SubmitField("Save Details")

