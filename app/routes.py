from flask import current_app as app, render_template

from .controller import create_token


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/create')
def create():
    token_id = create_token()
    return 'Created token: {}'.format(token_id)
