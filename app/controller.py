from .models import db, Token


def create_token():
    token1 = Token(
        token="123",
        channels="bios"
    )
    db.session.add(token1)
    db.session.commit()
    return str(token1.id)
