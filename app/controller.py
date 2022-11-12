import secrets

from .models import db, Token


def create_token():
    generated_token = secrets.token_hex(16)
    token = Token(
        token=generated_token,
        channels="bios"
    )
    db.session.add(token)
    db.session.commit()
    return generated_token
