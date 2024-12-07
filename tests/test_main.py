# tests/test_main.py

from fastapi.testclient import TestClient


def test_root(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200, response.json()
    response_data = response.json()
    assert "Info" in response_data
    assert response_data["Info"] == "Personal API"
