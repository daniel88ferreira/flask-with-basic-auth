import os.path

from flask_testing import TestCase

from app.models import Token, db

here = os.path.realpath(os.path.basename(__name__))


class TestModels(TestCase):

    def create_app(self):
        from app.main import create_app
        app = create_app(
            {"SQLALCHEMY_DATABASE_URI": "sqlite://", "TESTING": True}
        )
        return app

    def test_token(self):
        token = Token(
            token="123",
            channels="bios"
        )
        db.session.add(token)
        db.session.commit()

        assert token in db.session

    def setUp(self):
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
