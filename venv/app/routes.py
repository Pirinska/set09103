from click import password_option
from flask import Flask, request, render_template, flash, Blueprint, redirect, url_for
from flask_login import current_user, login_user, logout_user
from .models import User
from flask_login import login_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

views = Blueprint('views', __name__)


@views.route('/',  methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('inputPassword')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged successfully')
                login_user(user, remember=True)
                return redirect(url_for('views.index'))

            else:
                flash('Try again', category='error')
        else:
            flash('Email does not exist', category='error')

    return render_template('login.html', title='Login', user=current_user)


@views.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')
        elif len(email) < 5:
            flash('Email must have more than 5 characters', category='error')
        elif password1 != password2:
            flash('Your passwords do not match', category='error')
        elif len(password1) < 8:
            flash('Your password need to be 8 or more characters.', category='error')
        else:
            new_user = User(email=email, password=generate_password_hash(
                password1, method='sha256'), first_name=first_name,)
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('You registered successfully', category='success')
            return redirect(url_for('views.index'))
    return render_template('register.html', title='Register', user=current_user)


@views.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.login'))


@views.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html', title='Home', user=current_user)


@views.route('/calculate')
@login_required
def calculate():
    return render_template('calculate.html', title='Calculate', user=current_user)


@views.route('/plan')
@login_required
def plan():
    return render_template('plan.html', title='Plan', user=current_user)


@views.route('/userProfile')
@login_required
def userProfile():
    return render_template('userProfile.html', title='User Profile', user=current_user)
