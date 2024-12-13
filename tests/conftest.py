# tests/conftest.py

from fastapi.testclient import TestClient
from pytest import fixture

from src.database import get_session
from src.main import app as test_app
from tests.common.database import get_test_session


@fixture(scope="session")
def start_up_client():
    test_app.dependency_overrides[get_session] = get_test_session
    with TestClient(test_app) as client:
        response = client.get("/")
        assert response.status_code == 200, response.json()
        response_data = response.json()
        assert "message" in response_data
        assert "Personal API" in response_data["message"]
        yield client


@fixture(scope="function")
def client(start_up_client: TestClient):
    yield start_up_client
