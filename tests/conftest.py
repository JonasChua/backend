# tests/conftest.py

from fastapi.testclient import TestClient
from pytest import fixture

from src.main import app


@fixture
def client():
    yield TestClient(app)
