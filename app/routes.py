from flask import current_app as app, render_template

from .controller import create_token


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/create')
def create():
    return str(create_token())
