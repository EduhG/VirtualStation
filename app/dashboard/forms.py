from flask_wtf import Form
from wtforms import SubmitField, validators, StringField, RadioField, TextAreaField

from .models import ReportedCase


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


class CaseNotesForm(Form):
    search_input = StringField("Email", [validators.DataRequired("Please enter Ref Id to search.")])
    add_notes = TextAreaField('Description', [validators.DataRequired("Please enter notes to update.")])

    submit = SubmitField("Save Notes")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        ref_id = ReportedCase.query.filter_by(id=self.search_input.data).first()

        if ref_id:
            return True
        else:
            self.search_input.errors.append("Ref Number not found")
            return False
