from flask import render_template, request, url_for, redirect, flash
from flask_login import login_required, login_user
from forms import NewCaseForm
from .models import ReportedCase
from . import dashboard


@dashboard.route('/dashboard')
@login_required
def dashboard():
    return render_template('auth/signin.html')


@dashboard.route('/newcase', methods=['GET', 'POST'])
@login_required
def newcase():
    form = NewCaseForm()

    if form.validate_on_submit():
        user = ReportedCase.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
        return redirect(request.args.get('next') or url_for('dashboard.newcase'))
        flash('Invalid username or password.')
    return render_template('dashboard/new-case.html', form=form)

