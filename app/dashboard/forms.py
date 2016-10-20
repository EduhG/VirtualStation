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
    add_search_id = StringField("Email", [validators.InputRequired("Please enter Ref Id to search.")])
    add_notes = TextAreaField('Description', [validators.InputRequired("Please enter notes to update."),
                                              validators.Length(10, 1000)])

    submit = SubmitField("Save Notes")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):

        ref_id = ReportedCase.query.filter_by(id=self.add_search_id.data).first()

        if ref_id and len(self.add_notes.data) > 10:
            return True
        else:
            return False


class CloseCaseForm(Form):
    add_close_id = StringField('Case Id', [validators.InputRequired("Case Id can not be empty.")])
    add_close_notes = TextAreaField('Description', [validators.InputRequired("Please enter notes to update.")])

    submit = SubmitField("Save to Close")
