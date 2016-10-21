from flask import render_template, request, session, url_for, redirect, flash
from flask_login import logout_user, login_required, login_user
from forms import SigninForm
from .models import User
from . import auth


@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
        return redirect(request.args.get('next') or url_for('dashboard.index'))
        flash('Invalid username or password.')
    return render_template('auth/signin.html', form=form)


@auth.route('/signout')
@login_required
def signout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('home.index'))


@auth.route('/create_account', methods=['GET', 'POST'])
def create_account():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
