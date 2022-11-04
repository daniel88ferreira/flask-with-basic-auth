from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String, nullable=False)
    channels = db.Column(db.String, default='', nullable=False)

    def __repr__(self):
        return "<Token {}>".format(self.id)


@app.route('/', )
def index():
    return 'Hello World!'


def main():
    with app.app_context():
        db.create_all()
    app.run()
