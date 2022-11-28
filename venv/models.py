# Importing needed libraries and database
from flask_login import UserMixin
import sqlalchemy
from . import db
from sqlalchemy.sql import func

# The database consists of three tables User, Todo (storing upcoming workouts) and Measurelogs (Measurement history).
# Both the Measurelogs and Todo have one-to-many relashionships with the User table. One user can have many todo items and many measurelogs.


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(100))
    todos = db.relationship('Todo')
    measurelogs = db.relationship('MeasureLogs')


class MeasureLogs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.String(50))
    weight = db.Column(db.String(50))
    hips = db.Column(db.String(50))
    waist = db.Column(db.String(50))
    upper_arm = db.Column(db.String(50))
    chest = db.Column(db.String(50))
    thigh = db.Column(db.String(50))
    calf = db.Column(db.String(50))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

