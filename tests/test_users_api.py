# test Users REST API

import pytest
import json
from reviews_service.init import app
from reviews_service.__main__ import initialize
from reviews_service.users import get_user_service


@pytest.fixture
def user():
    return {
        "name": "testwebuser",
        "password": "test password",
        "email": "testweb@test.com"
    }


@pytest.fixture
def flask_client():

    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        initialize()
        get_user_service().erase_all()

    yield client


def test_add_user(flask_client, user):
    """ Happy path for the OAuth refresh token"""
    rv = flask_client.post("/api/users/", data=json.dumps(user), headers={'Content-Type': 'application/json'})
    assert rv._status_code == 200
    response_ = rv.json
    assert response_["name"] == user["name"]
    assert response_["email"] == user["email"]
    assert int(response_["id"]) > 0

