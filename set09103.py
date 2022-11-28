# from .routes import views, db
# from app.models import User, Todo, MeasureLogs

# # The shell processor allows to use Python commands and retrieve data from the database


# @views.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'User': User, 'Todo': Todo, 'MeasureLogs': MeasureLogs}

from venv import create_app

app = create_app()

if __name__ == '__main__':
    app.run()

