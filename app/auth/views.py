from flask import render_template, request, session, url_for, redirect, flash
from flask_login import logout_user, login_required, login_user
from forms import SigninForm, SignupForm
from ..utils.username import generate_username
from .models import User
from .. import db
from . import auth


@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
        return redirect(request.args.get('next') or url_for('home.index'))
        flash('Invalid username or password.')
    return render_template('auth/signin.html', form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        first = form.first_name.data
        last = form.other_names.data

        user = User(email=form.email.data,
                    username=generate_username(first, last),
                    first_name=form.first_name.data,
                    other_names=form.other_names.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()

        flash('Your account has been created successfully.')
        return redirect(url_for('auth.signin'))
    return render_template('auth/signup.html', form=form)


@auth.route('/signout')
@login_required
def signout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('home.index'))

