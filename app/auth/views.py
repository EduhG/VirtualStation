from flask import render_template, request, session, url_for, redirect
from forms import SigninForm
from . import auth


@auth.route('/auth/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()

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
