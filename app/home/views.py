from flask import render_template, url_for, redirect
from . import home


@home.route('/')
def index():
    # return render_template('index.html')
    return redirect(url_for('auth.signin'))

