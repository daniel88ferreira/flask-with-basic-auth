from .main import db


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String, nullable=False)
    channels = db.Column(db.String, default='', nullable=False)

    def __repr__(self):
        return "Token {}".format(self.id)
