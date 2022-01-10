# Users DB Model

from reviews_service.init import db
from sqlalchemy.orm import validates
from reviews_service.exceptions import ValidationError


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # TODO: do not store clear text passwords, store hash instead
    password = db.Column(db.String(80), unique=False, nullable=False)

    @staticmethod
    def init():
        db.create_all()

    @validates('password')
    def validate_some_string(self, key, password) -> str:
        if len(password) < 8:
            raise ValidationError('password too short, minimal password length is 8 characters')
        return password