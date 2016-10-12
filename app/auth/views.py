from flask import render_template, request, session, url_for, redirect, flash
from flask_login import logout_user, login_required, login_user
from forms import SigninForm
from .models import User
from . import auth


@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()

    # if form.validate() is True:
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
        return redirect(request.args.get('next') or url_for('home.index'))
        flash('Invalid username or password.')
    return render_template('auth/signin.html', form=form)

    """
    if 'loginid' in session:
        print session['loginid']
        return redirect(url_for('home.index'))

    if request.method == 'POST':
        if form.validate() is False:
            return render_template('auth/signin.html', form=form)
        else:
            session['loginid'] = form.email.data
            return redirect(url_for('home.index'))

    elif request.method == 'GET':
        return render_template('auth/signin.html', form=form)
"""


@auth.route('/signout')
@login_required
def signout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('home.index'))
