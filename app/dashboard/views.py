from flask import render_template, request, url_for, redirect, flash
from flask_login import login_required
from sqlalchemy import func
from forms import NewCaseForm
from .. import db
from .models import ReportedCase, ComplaintTypes
from . import dashboard


@dashboard.route('/')
@login_required
def index():
    return render_template('dashboard/dashboard.html', complaints=get_complaint_type_count())


@dashboard.route('/newcase', methods=['GET', 'POST'])
@login_required
def newcase():
    form = NewCaseForm()

    if form.validate_on_submit():
        id_method = request.form['id_method']
        id_number = request.form['id_number']
        first_name = request.form['first_name']
        other_names = request.form['other_names']
        gender = request.form['gender']
        phone_number = request.form['phone_number']
        email = request.form['email']
        reg_date = request.form['reg_date']
        complaint_type = request.form['complaint_type']
        description = request.form['description']

        newstudent = ReportedCase(id_method, id_number, first_name, other_names, gender,
                                  phone_number, email, reg_date, complaint_type, description)
        db.session.add(newstudent)
        db.session.commit()

        flash('Invalid username or password.')
        return redirect(request.args.get('next') or url_for('dashboard.newcase'))

    return render_template('dashboard/new-case.html', form=form)


def get_complaint_type_count():
    complaints = {}

    for complaint in db.session.query(ComplaintTypes).all():
        count = db.session.query(ReportedCase).filter_by(complaint_type=complaint.complaint).count()
        complaints[complaint.complaint] = count

    return complaints
