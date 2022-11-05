from flask_testing import TestCase

from app.models import Token, db


class TestModels(TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        from app.main import create_app
        app = create_app()
        app.config["SQLALCHEMY_DATABASE_URI"] = self.SQLALCHEMY_DATABASE_URI
        return app

    def test_token(self):
        token1 = Token(
            token="123",
            channels="bios"
        )
        db.session.add(token1)
        db.session.commit()

        assert token1 in db.session

    def setUp(self):
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
