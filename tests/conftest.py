# tests/conftest.py

from logging import getLogger
from fastapi.testclient import TestClient
from pytest import fixture

from src.database import get_session
from src.main import app as test_app
from tests.common.database import get_test_session

logger = getLogger(__name__)
test_app.dependency_overrides[get_session] = get_test_session


@fixture(scope="session")
def start_up_client():
    with TestClient(test_app) as client:
        response = client.get("/")
        assert response.status_code == 200, response.json()
        response_data = response.json()
        assert "Info" in response_data
        assert response_data["Info"] == "Personal API"
        yield client


@fixture(scope="function")
def client(start_up_client: TestClient):
    yield start_up_client
