from app.models import Todo, User
from flask import request, render_template, redirect, flash, url_for
from app import app
from app.form import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.models import User


@app.route('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
        
    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))
    
@app.route('/register')
def register():
    return render_template('register.html', title='Register', todo=Todo)
        
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home', todo=Todo)

@app.route('/calculate')
def calculate():
    return render_template('calculate.html', title='Calculate', todo=Todo)

@app.route('/plan')
def plan():
    return render_template('plan.html', title='Plan', todo=Todo)

@app.route('/userProfile')
def userProfile():
    return render_template('userProfile.html', title='User Profile', todo=Todo)

