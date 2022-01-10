# User Manager
from reviews_service.exceptions import AlreadyExistError, NotFoundError
from sqlalchemy.exc import IntegrityError
from .model import UserModel


class UserController:
    def __init__(self):
        self._model = UserModel()

    def init(self):
        self._model.init()

    def add(self, user):
        """
        Add new user
        :param user: dictionary with user data
        :return user id as integer
        """
        try:
            return self._format_user(self._model.add(user))
        except IntegrityError as exc:
            err_ = str(exc)
            msg = f"user with name {user['name']} already exists" if "user.name" in err_ else \
                f"user with email {user['email']} already exists"
            raise AlreadyExistError(msg)

    def get_by_name(self, name):
        user_ = self._model.get_by_name(name)
        if not user_:
            raise NotFoundError(f'user {name} not found')
        return self._format_user(user_)

    def get_all(self):
        # do not return password for security reason
        users_ = [self._format_user(user) for user in self._model.get_all()]
        return users_

    @staticmethod
    def _format_user(db_user):
        return {"id": db_user.id,
                "name": db_user.name,
                "email": db_user.email,
                }

    def delete_by_name(self, name):
        self._model.delete_by_name(name)

    def erase_all(self):
        self._model.erase_all()


controller_ref = UserController()


def get_user_service():
    return controller_ref
