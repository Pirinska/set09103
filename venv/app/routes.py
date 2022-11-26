import json
from click import password_option
from flask import Flask, jsonify, request, render_template, flash, Blueprint, redirect, url_for
from flask_login import current_user, login_user, logout_user
from .models import User, Todo, MeasureLog
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
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user, remember=True)
            flash('You registered successfully', category='success')
            return redirect(url_for('views.index'))
    return render_template('register.html', title='Register', user=current_user)


@views.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.login'))


@views.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html', title='Home', user=current_user)


@views.route('/calculate', methods=['GET', 'POST'])
@login_required
def calculate():
    return render_template('calculate.html', title='Calculate', user=current_user)


@views.route('/plan', methods=['GET', 'POST'])
@login_required
def plan():
    if request.method == 'POST':
        todo = request.form.get('todo')

        if len(todo) < 3:
            flash('Text is too short!', category='error')
        else:
            new_todo = Todo(body=todo, user_id=current_user.id)
            db.session.add(new_todo)
            db.session.commit()
            flash('Wohoo, you added a workout!', category='success')

    return render_template('plan.html', title='Plan', user=current_user)


@views.route('/delete-todo', methods=['GET', 'POST'])
def delete_todo():
    todo = json.loads(request.data)
    todoId = todo['todoId']
    todo = Todo.query.get(todoId)
    if todo:
        if todo.user_id == current_user.id:
            db.session.delete(todo)
            db.session.commit()

    return jsonify({})


@views.route('/userProfile', methods=['GET', 'POST'])
@login_required
def userProfile():
    if request.method == 'POST':
        height1 = request.form.get('height')
        weight1 = request.form.get('weight')
        hips1 = request.form.get('hips')
        waist1 = request.form.get('waist')
        upper_arm1 = request.form.get('upper_arm')
        chest1 = request.form.get('chest')
        thigh1 = request.form.get('thigh')
        calf1 = request.form.get('calf')

            if len(height1) < 2:
                flash('Text is too short!', category='error')
            else:
                new_measure_log = MeasureLog(height=height1, weight=weight1, hips=hips1, waist=waist1, upper_arm=upper_arm1, chest=chest1, thigh=thigh1, calf=calf1, user_id=current_user.id)
                db.session.add(new_measure_log)
                db.session.commit()
                flash('Wohoo, you added new measurement!', category='success')

    return render_template('userProfile.html', title='User Profile', user=current_user)
