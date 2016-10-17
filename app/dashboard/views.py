from flask import render_template, request, url_for, redirect, flash
from flask_login import login_required, login_user
from forms import NewCaseForm
from .models import ReportedCase
from . import dashboard


@dashboard.route('/')
@login_required
def index():
    return render_template('dashboard/dashboard.html')


@dashboard.route('/newcase', methods=['GET', 'POST'])
@login_required
def newcase():
    form = NewCaseForm()

    if form.validate_on_submit():
        """user = ReportedCase.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
        return redirect(request.args.get('next') or url_for('dashboard.newcase'))
        flash('Invalid username or password.')"""
        pass
    return render_template('dashboard/new-case.html', form=form)

