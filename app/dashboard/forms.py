from flask_wtf import FlaskForm, Form
from wtforms import SubmitField, validators, StringField, RadioField, TextAreaField, ValidationError
from wtforms_components import read_only
from ..auth.models import User

from .models import ReportedCase, CaseTypes


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


class CloseCaseForm(FlaskForm):
    add_close_id = StringField('Case Id', [validators.InputRequired("Case Id can not be empty.")])
    add_close_name = StringField('Full Name', [validators.InputRequired("Case Id can not be empty.")])
    add_close_notes = TextAreaField('Description', [validators.InputRequired("Please enter notes to update.")])

    submit = SubmitField("Save to Close")

    def __init__(self, *args, **kwargs):
        super(CloseCaseForm, self).__init__(*args, **kwargs)
        read_only(self.add_close_id)
        read_only(self.add_close_name)


class CaseTypesForm(FlaskForm):
    cartegory_name = StringField("Cartegory Name", [validators.InputRequired("Please enter Ref Id to search.")])

    submit = SubmitField("Save Cartegory")

    def __init__(self, *args, **kwargs):
        super(CaseTypesForm, self).__init__(*args, **kwargs)

    def validate(self):

        cartegory = CaseTypes.query.filter_by(complaint=self.cartegory_name.data).first()

        if not cartegory:
            return True
        else:
            new_errors = list(self.cartegory_name.errors)
            new_errors.append("Cartegory already exists")
            self.cartegory_name.errors = tuple(new_errors)

            return False


class CreateAccountForm(FlaskForm):
    first_name = StringField('First Name', [validators.DataRequired("Please enter your first name.")])
    other_names = StringField("Other Names", [validators.DataRequired("Please enter your other names.")])
    email = StringField("Email", [validators.DataRequired("Please enter your email address."),
                        validators.Email("Please enter your email address.")])

    submit = SubmitField("Sign Up")

    def __init__(self, *args, **kwargs):
        super(CreateAccountForm, self).__init__(*args, **kwargs)

    def validate(self):
        user = User.query.filter_by(email=self.email.data.lower()).first()
        if user:
            self.email.errors.append("That email is already taken")
            return False
        else:
            return True
