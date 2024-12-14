# tests/api/test_token.py

from fastapi.testclient import TestClient

from tests.common.utility import parse_error
from tests.data.user import test_user_a


def test_getToken_successful(client: TestClient):
    response = client.post(
        "/token",
        headers={"content-type": "application/x-www-form-urlencoded"},
        data={
            "grant_type": "password",
            "username": test_user_a["username"],
            "password": test_user_a["password"],
        },
    )
    response_data = response.json()
    assert response.status_code == 200, response_data
    assert "token_type" in response_data
    assert response_data["token_type"] == "Bearer"


def test_getToken_userNotFound(client: TestClient):
    response = client.post(
        "/token",
        headers={"content-type": "application/x-www-form-urlencoded"},
        data={
            "grant_type": "password",
            "username": "invalidUsername",
            "password": test_user_a["password"],
        },
    )
    response_data = response.json()
    assert response.status_code == 404, response_data
    error_code, message = parse_error(response_data)
    assert error_code
    assert "User" in message and "not found" in message


def test_getToken_invalidPassword(client: TestClient):
    response = client.post(
        "/token",
        headers={"content-type": "application/x-www-form-urlencoded"},
        data={
            "grant_type": "password",
            "username": test_user_a["username"],
            "password": "invalidPassword",
        },
    )
    response_data = response.json()
    assert response.status_code == 401, response_data
    error_code, message = parse_error(response_data)
    assert error_code
    assert "Invalid username or password" in message
