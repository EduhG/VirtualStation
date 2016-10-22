from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user
from app.dashboard.models import ReportedCase, CaseNotes
from . import home
from .. import db


@home.route('/')
def index():
    return render_template('index.html')


def get_case_notes():
    case_notes_list = []
    print current_user.email

    for case in db.session.query(ReportedCase).filter_by(email=current_user.email).all():

        case_id = case.id
        case_desc = case.description

        reported_cases = {'id': case_id, 'description': case_desc}

        case_notes = [notes.notes for notes in db.session.query(CaseNotes).filter_by(ref_id=case_id).all()]

        reported_cases['notes'] = case_notes

        reported_cases['notes_count'] = len(case_notes)

        case_notes_list.append(reported_cases)

    print case_notes_list

    return case_notes_list


@home.route('/my_search_results')
def my_search_results():
    search_results = []

    ref_id = request.args.get('search_id')
    print 'my_search_results => ', ref_id

    for case_notes in db.session.query(CaseNotes).filter_by(ref_id=ref_id).all():
        found = {'notes': case_notes.notes}

        search_results.append(found)

    return render_template('search_results.html', search_results=search_results)


@home.route('/mycases')
@login_required
def my_cases():
    return render_template('mycases.html', cases_notes=get_case_notes())

