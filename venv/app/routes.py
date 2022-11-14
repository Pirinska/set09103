from flask import Flask, request, render_template
from app import app

@app.route('/')

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

