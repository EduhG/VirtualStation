from flask import render_template, request, url_for, redirect, flash, jsonify
from flask_login import login_required
from datetime import date, datetime, timedelta
import calendar
from ..utils.custom_calendar import months_days, str_to_date
from forms import NewCaseForm
from .. import db
from .models import ReportedCase, ComplaintTypes
from . import dashboard

now = datetime.now()


def a_day_in_previous_month(dt):
    return datetime(dt.year, dt.month, 1) - timedelta(days=1)


def last_day_of_month():
    c_date = date.today()
    start_date = datetime(c_date.year, c_date.month, 1)
    end_date = datetime(c_date.year, c_date.month, calendar.mdays[c_date.month])
    print start_date, end_date


def first_day_of_month(dt):
    return date(dt.year, dt.month, 1)


def get_complaint_type_count():
    complaints = {}

    for complaint in db.session.query(ComplaintTypes).all():
        count = db.session.query(ReportedCase).filter_by(complaint_type=complaint.complaint).count()
        complaints[complaint.complaint] = count

    return complaints


def get_reported_cases():
    reported_cases_summary = {}

    dt = datetime.strptime(datetime.now().date().strftime('%Y-%m-%d'), '%Y-%m-%d')
    c_date = date.today()
    start_date = datetime(c_date.year, c_date.month, 1)
    end_date = datetime(c_date.year, c_date.month, calendar.mdays[c_date.month])

    current_month_count = db.session.query(ReportedCase).filter(
        ReportedCase.reported_date.between(start_date, end_date)).count()

    reported_cases_summary["current_month"] = current_month_count

    last_month_count = db.session.query(ReportedCase).filter(
        ReportedCase.reported_date.between(
            first_day_of_month(a_day_in_previous_month(dt)), a_day_in_previous_month(dt))).count()

    reported_cases_summary["last_month"] = last_month_count

    diff = current_month_count - last_month_count
    total = current_month_count + last_month_count
    if diff > 0:
        change = (diff * 100) / total
    else:
        change = 0

    reported_cases_summary["change"] = change

    print reported_cases_summary

    return reported_cases_summary


@dashboard.route('/reported_cases_chart')
def reported_cases_chart():
    comps = []

    for complaint in db.session.query(ComplaintTypes).all():
        complaints = {}

        count = db.session.query(ReportedCase).filter_by(complaint_type=complaint.complaint).count()
        print complaint.complaint, " => ", count
        complaints["complaint"] = complaint.complaint
        complaints["total_count"] = count

        comps.append(complaints)

    response = jsonify(comps)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@dashboard.route('/total_reported_cases_annually')
def total_reported_cases_annually():
    comps = months_days(date.today().year)

    monthly = []

    for comp in comps:
        for key, value in comp.iteritems():
            year_start = value['first_date']
            year_end = value['last_date']

            details = {}

            monthly_count = db.session.query(ReportedCase).filter(
                ReportedCase.reported_date.between(year_start, year_end)).count()

            details['calendar_month'] = key
            details['month_count'] = monthly_count

            monthly.append(details)

    print monthly

    response = jsonify(monthly)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


def current_date():
    return '{} {} {}'.format(date.today().strftime("%B"), str(now.day) + ',', now.year)


@dashboard.route('/')
@login_required
def index():
    return render_template('dashboard/dashboard.html', complaints=get_complaint_type_count(),
                           current_date=current_date(), reported_cases=get_reported_cases())


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
        reg_date = str_to_date(request.form['reg_date'])
        complaint_type = request.form['complaint_type']
        description = request.form['description']

        #print reg_date.split()

        newstudent = ReportedCase(id_method, id_number, first_name, other_names, gender,
                                  phone_number, email, reg_date, complaint_type, description)
        db.session.add(newstudent)
        db.session.commit()

        flash('Invalid username or password.')
        return redirect(request.args.get('next') or url_for('dashboard.newcase'))

    return render_template('dashboard/new-case.html', form=form)


@dashboard.route('/list_cases')
@login_required
def list_cases():
    return render_template('dashboard/list-cases.html')


@dashboard.route('/notes')
@login_required
def notes():
    return render_template('dashboard/list-cases.html')


@dashboard.route('/administrator')
@login_required
def administrator():
    return render_template('dashboard/list-cases.html')
