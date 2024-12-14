# tests/api/conftest.py

from fastapi.testclient import TestClient
from pytest import fixture

from src.common.authentication import encode_jwt_token
from tests.data.user import test_user_a, test_user_b, create_user, delete_user


@fixture(scope="function")
def client(start_up_client: TestClient):
    create_user(test_user_a)
    yield start_up_client
    delete_user(test_user_a)
    delete_user(test_user_b)


@fixture(scope="package")
def token_headers():
    def __token_headers() -> dict[str, dict[str, str]]:
        headers: dict[str, dict[str, str]] = {}
        headers["test_user_a"] = {
            "authorization": f"Bearer {encode_jwt_token({"sub": test_user_a["username"]})}"
        }
        headers["test_user_b"] = {
            "authorization": f"Bearer {encode_jwt_token({"sub": test_user_b["username"]})}"
        }
        headers["invalid_user"] = {
            "authorization": f"Bearer {encode_jwt_token({"sub": "invalid_user"})}"
        }
        headers["missing_subject"] = {"authorization": f"Bearer {encode_jwt_token({})}"}
        headers["invalid_token"] = {"authorization": "Bearer invalidToken"}
        return headers

    yield __token_headers()
