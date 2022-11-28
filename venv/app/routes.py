import json
from click import password_option
from flask import Flask, jsonify, request, render_template, flash, Blueprint, redirect, url_for
from flask_login import current_user, login_user, logout_user
import requests
from .models import User, Todo, MeasureLogs
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

    return render_template('login.html', title='Login', user=current_user, page=-1)


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
    return render_template('register.html', title='Register', user=current_user, page=-2)


@views.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.login'))


@views.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    res = requests.get(
        f'http://api.mediastack.com/v1/news?access_key=9ac9b232ed136147d61e2df0eb305548&keywords=workout&categories=health&countries=us,gb,ca,au')
    if res.status_code == 200:
        news_data = res.json()
        return render_template("index.html", news_data=news_data['data'], title='Home', user=current_user, page=0)
    else:
        return render_template('index.html', title='Home', user=current_user, page=0)


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
            return redirect(url_for('views.plan'))
        return render_template('plan.html', title='User Profile', user=current_user, page=2)



@views.route('/userProfile', methods=['GET', 'POST'])
@login_required
def userProfile():
        if request.method == 'POST':
            height = request.form.get('height')
            weight = request.form.get('weight')
            hips = request.form.get('hips')
            waist = request.form.get('waist')
            upper_arm = request.form.get('upper_arm')
            chest = request.form.get('chest')
            thigh = request.form.get('thigh')
            calf = request.form.get('calf')
            if len(height) < 2:
                flash('Text is too short!', category='error')
            else:
                new_measure_log = MeasureLogs(height=height, weight=weight, hips=hips, waist=waist,
                                          upper_arm=upper_arm, chest=chest, thigh=thigh, calf=calf, user_id=current_user.id)
                db.session.add(new_measure_log)
                db.session.commit()
                flash('Wohoo, you added new measurement!', category='success')
            return redirect(url_for('views.userProfile'))
        return render_template('userProfile.html', title='User Profile', user=current_user, page=3)


@views.route('/delete-todo', methods=['GET', 'POST'])
@login_required
def delete_todo():
    todo = json.loads(request.data)
    todoId = todo['todoId']
    todo = Todo.query.get(todoId)
    if todo:
        if todo.user_id == current_user.id:
            db.session.delete(todo)
            db.session.commit()

    return jsonify({})

@views.route('/deletemeasurelog', methods=['GET', 'POST'])
@login_required
def delete_measurelog():
    measurelog = json.loads(request.data)
    measurelogId = measurelog['measurelogId']
    measurelog = MeasureLogs.query.get(measurelogId)
    if measurelog:
        if measurelog.user_id == current_user.id:
            db.session.delete(measurelog)
            db.session.commit()

    return jsonify({})


@views.route('/calculate', methods=['GET', 'POST'])
@login_required
def calculate():
    return render_template('calculate.html', title='User Profile', user=current_user, page=1)


@views.route('/bmicm', methods=['GET', 'POST'])
@login_required
def calculateBMIcm():
    bmicm = ''
    if request.method == 'POST' and 'heightcm' in request.form and 'weightkg1' in request.form:
        heightBMIcm = float(request.form.get('heightcm'))
        weightBMIkg = float(request.form.get('weightkg1'))
        bmicm = round(weightBMIkg/((heightBMIcm/100)**2), 2)

    return render_template('calculate.html', title='User Profile', user=current_user, bmicm=bmicm, page=1)

@views.route('/bmiinch', methods=['GET', 'POST'])
@login_required
def calculateBMIinch():
    bmiinch = ''
    if request.method == 'POST' and 'heightinch' in request.form and 'weightpounds' in request.form:
        heightBMIinch = float(request.form.get('heightinch'))
        weightBMIpounds = float(request.form.get('weightpounds'))
        bmiinch = round(((weightBMIpounds/(heightBMIinch**2))*703), 2)

    return render_template('calculate.html', title='User Profile', user=current_user, bmicm=bmiinch, page=1)

