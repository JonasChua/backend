# tests/api/test_user.py

from fastapi.testclient import TestClient

from tests.common.utility import parse_error
from tests.data.user import test_user_a, test_user_b


def test_getUser_success(client: TestClient):
    response = client.get(f"/user/{test_user_a["username"]}")
    response_data = response.json()
    assert response.status_code == 200, response_data
    for key, value in test_user_a.items():
        assert response_data[key] == value


def test_getUser_userNotFound(client: TestClient):
    response = client.get("/user/invalidUsername")
    response_data = response.json()
    assert response.status_code == 404, response_data
    error_code, message = parse_error(response_data)
    assert error_code
    assert "User" in message and "not found" in message


def test_createUser_success(client: TestClient):
    response = client.post("/user", json=test_user_b)
    response_data = response.json()
    assert response.status_code == 200, response_data
    for key, value in test_user_b.items():
        assert response_data[key] == value


def test_createUser_userAlreadyExist(client: TestClient):
    response = client.post("/user", json=test_user_a)
    response_data = response.json()
    assert response.status_code == 409, response_data
    error_code, message = parse_error(response_data)
    assert error_code
    assert "User" in message and "already exists" in message
