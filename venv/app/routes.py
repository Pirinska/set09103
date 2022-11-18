from flask import request, render_template, redirect, flash, url_for
from app import app
from app.form import LoginForm


@app.route('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
    
@app.route('/register')
def register():
    user = {'username': 'Vili'}
    return render_template('register.html', title='Register', user=user)
        

@app.route('/index')
def index():
    user = {'username': 'Vili'}
    return render_template('index.html', title='Home', user=user)

@app.route('/calculate')
def calculate():
    user = {'username': 'Vili'}
    return render_template('calculate.html', title='Calculate', user=user)

@app.route('/plan')
def plan():
    user = {'username': 'Vili'}
    return render_template('plan.html', title='Plan', user=user)

@app.route('/userProfile')
def userProfile():
    user = {'username': 'Vili'}
    return render_template('userProfile.html', title='User Profile', user=user)

