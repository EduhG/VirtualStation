from .. import db
from datetime import datetime


class ReportedCase(db.Model):
    __tablename__ = 'reported_cases'

    id = db.Column(db.Integer, primary_key=True)
    id_method = db.Column(db.String(100))
    id_number = db.Column(db.String(64), unique=True)
    first_name = db.Column(db.String(100))
    other_names = db.Column(db.String(100))
    gender = db.Column(db.String(20))
    phone_number = db.Column(db.String(20))
    email = db.Column(db.String(64), unique=True)
    reg_date = db.Column(db.Date(), default=datetime.now().date())
    reported_date = db.Column(db.Date(), default=datetime.now().date())
    complaint_type = db.Column(db.String(100))
    description = db.Column(db.String(1000))

    case_closed = db.Column(db.Boolean, default=False)
    closed_by = db.Column(db.String(200))
    closed_date = db.Column(db.Date(), default=None)

    def __init__(self, id_method, id_number, first_name, other_names, gender,
                 phone_number, email, reg_date, complaint_type, description):
        self.id_method = id_method
        self.id_number = id_number
        self.first_name = first_name
        self.other_names = other_names
        self.gender = gender
        self.phone_number = phone_number
        self.email = email
        self.reg_date = reg_date
        self.complaint_type = complaint_type
        self.description = description


class CaseTypes(db.Model):
    __tablename__ = 'case_types'

    id = db.Column(db.Integer, primary_key=True)
    complaint = db.Column(db.String(100), unique=True)

    def __init__(self, complaint):
        self.id_method = complaint


class CaseNotes(db.Model):
    __tablename__ = 'case_notes'

    id = db.Column(db.Integer, primary_key=True)
    ref_id = db.Column(db.Integer)
    notes = db.Column(db.String(10000))
    date_created = db.Column(db.Date(), default=datetime.now().date())
    created_by = db.Column(db.String(100))

    def __init__(self, ref_id, notes, created_by):
        self.ref_id = ref_id
        self.notes = notes
        self.created_by = created_by
