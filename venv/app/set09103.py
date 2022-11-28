from app import app, db
from app.models import User, Todo

# The shell processor allows to use Python commands and retrieve data from the database


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Todo': Todo}
