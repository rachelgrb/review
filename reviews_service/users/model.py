# Model

from reviews_service.init import db
from reviews_service.exceptions import NotFoundError
from .user import User


class UserModel:
    """
    DB Operations for the Users
    """
    def __init__(self):
        pass

    def init(self):
        # create DB
        User.init()

    def add(self, user):
        try:
            user_ = User(**user)
            db.session.add(user_)
            db.session.commit()
            return user_
        except Exception:
            db.session.rollback()
            raise

    def get_all(self):
        return User.query.all()

    def get_by_name(self, user_name):
        return User.query.filter_by(name=user_name).first()

    def erase_all(self):
        try:
            db.session.query(User).delete()
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise

    def delete_by_name(self, user_name):
        query_ = db.session.query(User).filter_by(name=user_name)
        # check if user exists
        if not query_.first():
            raise NotFoundError(f'user {user_name} not found')

        try:
            query_.delete()
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise
