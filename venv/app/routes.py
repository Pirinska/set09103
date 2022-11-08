from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Vesko'}
    return '''
    <html> 
    <head>
        <title>Home Page - Welcome</title>
    </head>
    <body>
        <h1>Welcome, ''' + user['username'] + '''!</h1>
    </body>

    </html> '''

