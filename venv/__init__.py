# Importing libraries from Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# SQLAlchemy is used to create the database
db = SQLAlchemy()
DB_NAME = "database.db"

# Creating the app and a secret key for securing signed data


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'IslippedOn1BananaOnce!'
    # SQLAlchemy is stored at DB_NAME
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # Initialising the database with the app
    db.init_app(app)

    from .routes import views
    # blueprint defines a colection of views
    app.register_blueprint(views, url_prefix='/')

    from .models import User, Todo, MeasureLogs

    from . import models

    with app.app_context():
        db.create_all()

    # Flask-Login provides user session management for Flask. It handles logging in ad out.
    login_manager = LoginManager()
    login_manager.login_view = 'views.login'
    login_manager.init_app(app)

    # User loading function
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
