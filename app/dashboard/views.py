from flask import render_template, request, url_for, redirect, flash, jsonify
from flask_login import login_required
from sqlalchemy import and_
from datetime import date, datetime, timedelta
import calendar
from flask_login import current_user
from ..utils.username import generate_username
from ..utils.custom_calendar import months_days, str_to_date
from forms import NewCaseForm, CaseNotesForm, CloseCaseForm, CaseTypesForm, CreateAccountForm
from .. import db
from .models import ReportedCase, CaseTypes, CaseNotes
from . import dashboard
from ..auth.models import User

now = datetime.now()


def a_day_in_previous_month(dt):
    return datetime(dt.year, dt.month, 1) - timedelta(days=1)


def last_day_of_month():
    c_date = date.today()
    start_date = datetime(c_date.year, c_date.month, 1)
    end_date = datetime(c_date.year, c_date.month, calendar.mdays[c_date.month])


def first_day_of_month(dt):
    return date(dt.year, dt.month, 1)


def get_complaint_type_count():
    complaints = {}

    for complaint in db.session.query(CaseTypes).all():
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

    return reported_cases_summary


def get_closed_cases():
    reported_cases_summary = {}

    dt = datetime.strptime(datetime.now().date().strftime('%Y-%m-%d'), '%Y-%m-%d')
    c_date = date.today()
    start_date = datetime(c_date.year, c_date.month, 1)
    end_date = datetime(c_date.year, c_date.month, calendar.mdays[c_date.month])

    current_month_count = db.session.query(ReportedCase).filter_by(case_closed=True).filter(
        ReportedCase.reported_date.between(start_date, end_date)).count()

    reported_cases_summary["current_month"] = current_month_count

    last_month_count = db.session.query(ReportedCase).filter_by(case_closed=True).filter(
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

    return reported_cases_summary


@dashboard.route('/reported_cases_chart')
def reported_cases_chart():
    comps = []

    for complaint in db.session.query(CaseTypes).all():
        complaints = {}

        count = db.session.query(ReportedCase).filter_by(complaint_type=complaint.complaint).count()
        complaints["complaint"] = complaint.complaint
        complaints["total_count"] = count

        comps.append(complaints)

    response = jsonify(comps)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@dashboard.route('/closed_cases_chart')
def closed_cases_chart():
    comps = []

    for complaint in db.session.query(CaseTypes).all():
        complaints = {}

        count = db.session.query(ReportedCase).filter_by(
            complaint_type=complaint.complaint).filter(ReportedCase.case_closed == True).count()
        # filter(and_(ReportedCase.complaint_type == complaint.complaint, ReportedCase.case_closed == 1))
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

    response = jsonify(monthly)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@dashboard.route('/search_reported_cases')
def search_reported_cases():
    search_results = []

    search_id = request.args.get('search_id')

    for case in db.session.query(ReportedCase).filter_by(id=search_id).all():
        found_details = {'first_name': case.first_name, 'other_names': case.other_names}

        search_results.append(found_details)

    response = jsonify(search_results)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@dashboard.route('/search_notes')
def search_notes():
    search_results = []

    ref_id = request.args.get('search_id')

    for case_notes in db.session.query(CaseNotes).filter_by(ref_id=ref_id).all():
        found = {'notes': case_notes.notes}

        search_results.append(found)

    return render_template('dashboard/notes_results.html', search_results=search_results)


@dashboard.route('/reported_cases_search')
def reported_cases_search():
    search_results = []

    ref_id = request.args.get('search_id')

    for case in db.session.query(ReportedCase).filter(ReportedCase.id_number.like('%'+ref_id+'%')).all():
        found = {
            'id': case.id,
            'id_number': case.id_number,
            'full_name': str(case.first_name) + " " + str(case.other_names),
            'reported_date': case.reported_date,
            'complaint_type': case.complaint_type
        }

        search_results.append(found)

    return render_template('dashboard/reported_cases_table.html', search_results=search_results)


def current_date():
    return '{} {} {}'.format(date.today().strftime("%B"), str(now.day) + ',', now.year)


@dashboard.route('/')
@login_required
def index():
    return render_template('dashboard/dashboard.html', complaints=get_complaint_type_count(),
                           current_date=current_date(), reported_cases=get_reported_cases(),
                           closed_cases=get_closed_cases())


def get_case_types():
    case_types_list = []
    for case_type in db.session.query(CaseTypes).all():
        case_types_list.append(case_type.complaint)
    return case_types_list


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

        newstudent = ReportedCase(id_method, id_number, first_name, other_names, gender,
                                  phone_number, email, reg_date, complaint_type, description)
        db.session.add(newstudent)
        db.session.commit()

        flash('Invalid username or password.')
        return redirect(request.args.get('next') or url_for('dashboard.newcase'))

    return render_template('dashboard/new-case.html', form=form, case_types=get_case_types())


@dashboard.route('/list_cases', methods=['GET', 'POST'])
@login_required
def list_cases():
    form = CloseCaseForm(request.form)
    search_results = []

    for case in db.session.query(ReportedCase).all():
        found = {
            'id': case.id,
            'id_number': case.id_number,
            'full_name': str(case.first_name) + " " + str(case.other_names),
            'reported_date': case.reported_date,
            'complaint_type': case.complaint_type
        }

        search_results.append(found)

    if request.method == 'POST' and form.validate():
        search_id = request.form['add_close_id']
        close_notes = request.form['add_close_notes']

        reported_case = ReportedCase.query.filter_by(id=search_id).first()

        reported_case.case_closed = True
        reported_case.closed_by = current_user.username
        reported_case.closed_date = date.today()

        db.session.commit()

        new_notes = CaseNotes(search_id, close_notes, current_user.username)
        db.session.add(new_notes)
        db.session.commit()

        flash('Invalid username or password.')
        return redirect(request.args.get('next') or url_for('dashboard.list_cases'))

    return render_template('dashboard/list-cases.html', search_results=search_results, form=form)


@dashboard.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
    form = CaseNotesForm()

    if form.validate_on_submit():
        search_id = request.form['add_search_id']
        add_notes = request.form['add_notes']

        new_notes = CaseNotes(search_id, add_notes, current_user.username)
        db.session.add(new_notes)
        db.session.commit()

        flash('Notes added successfully.')
        return redirect(request.args.get('next') or url_for('dashboard.notes'))

    return render_template('dashboard/notes.html', form=form)


def system_users():
    system_users_list = []
    for user in db.session.query(User).filter(User.role_id != 1).all():
        user_details = {
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'first_name': user.first_name,
            'other_names': user.other_names
        }

        system_users_list.append(user_details)
    return system_users_list


@dashboard.route('/administrator', methods=['GET', 'POST'])
@login_required
def administrator():
    account_form = CreateAccountForm()
    types_form = CaseTypesForm()

    print types_form.submit1.data

    if types_form.submit1.data and types_form.validate_on_submit() and types_form.validate():
        print 'types form'

        cartegory_name = request.form['cartegory_name']

        print 'cartegory => ', cartegory_name

        case_types = CaseTypes(cartegory_name)
        db.session.add(case_types)
        db.session.commit()

        flash('Notes added successfully.')
        return redirect(request.args.get('next') or url_for('dashboard.administrator'))

    if account_form.validate_on_submit() and account_form.validate():
        first = account_form.first_name.data
        last = account_form.other_names.data

        user = User(email=account_form.email.data,
                    username=generate_username(first, last),
                    first_name=account_form.first_name.data,
                    other_names=account_form.other_names.data,
                    role_id=int(request.form.get('account_type')),
                    password='Password01')
        db.session.add(user)

        return redirect(request.args.get('next') or url_for('dashboard.administrator'))

    return render_template('dashboard/admin_panel.html', types_form=types_form,
                           account_form=account_form, complaints=get_complaint_type_count(),
                           system_users=system_users())


@dashboard.route('/search_system_users')
def search_system_users():
    search_results = []

    username = request.args.get('username')

    for user in db.session.query(User).filter(User.username.like('%'+username+'%')).all():
        user_details = {
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'first_name': user.first_name,
            'other_names': user.other_names
        }

        search_results.append(user_details)

    return render_template('dashboard/search_users.html', search_results=search_results)
