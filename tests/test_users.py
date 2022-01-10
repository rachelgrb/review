import pytest
import copy
from reviews_service.users import get_user_service
from reviews_service.exceptions import AlreadyExistError, ValidationError, NotFoundError


@pytest.fixture
def controller():
    contr_ = get_user_service()
    contr_.init()
    contr_.erase_all()
    yield contr_
    contr_.erase_all()


@pytest.fixture
def user():
    return {
        "name": "test user",
        "password": "test password",
        "email": "test@test.com"
    }


@pytest.fixture
def user_with_empty_password():
    return {
        "name": "test empty password user",
        "password": "",
        "email": "testemp@test.com"
    }


def test_add_user(controller, user):
    # test that new user added to the DB
    controller.add(user)
    new_user = controller.get_by_name(user["name"])

    # password is not returned
    assert new_user["name"] == user["name"]
    assert new_user["email"] == user["email"]


def test_add_user_with_duplicate_name(controller, user):
    # test that user cannot be added with same user name
    controller.add(user)

    same_name_user = copy.deepcopy(user)
    same_name_user["email"] = "test2@test.com"

    with pytest.raises(AlreadyExistError, match=f"user with name {user['name']} already exists"):
        controller.add(same_name_user)


def test_add_user_with_duplicate_email(controller, user):
    # test that user cannot be added with same user name
    controller.add(user)

    same_email_user = copy.deepcopy(user)
    same_email_user["name"] = "new name"

    with pytest.raises(AlreadyExistError, match=f"user with email {user['email']} already exists"):
        controller.add(same_email_user)


def test_add_user_with_empty_password(controller, user_with_empty_password):
    with pytest.raises(ValidationError, match=f"password too short, minimal password length is 8 characters"):
        controller.add(user_with_empty_password)


def test_delete_user(controller, user):
    controller.add(user)
    # should succeed
    controller.get_by_name(user["name"])

    controller.delete_by_name(user["name"])

    # should fail
    with pytest.raises(NotFoundError):
        controller.get_by_name(user["name"])


def test_delete_non_exist_user(controller):
    # should fail with NotFoundError exception
    with pytest.raises(NotFoundError):
        controller.delete_by_name("invalid user name")
