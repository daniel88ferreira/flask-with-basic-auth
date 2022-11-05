from flask import current_app as app

from .models import db, Token


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/insert')
def insert():
    token1 = Token(
        token="123",
        channels="bios"
    )
    db.session.add(token1)
    db.session.commit()
    return 'Created token: {}'.format(str(token1))
