from flask import Flask, request, render_template
from app import app



@app.route('/')


@app.route('/register', methods=['GET', 'post'])
def register():
    return render_template('register.html', title='Register')

@app.route('/login',  methods=['GET', 'post'])
def login():
    return render_template('login.html', title='Login')


@app.route('/index')
def index():
    
    return render_template('index.html', title='Home')

@app.route('/calculate')
def calculate():
    
    return render_template('calculate.html', title='Calculate')

@app.route('/plan')
def plan():
    
    return render_template('plan.html', title='Plan')

@app.route('/userProfile')
def userProfile():
    
    return render_template('userProfile.html', title='User Profile')


