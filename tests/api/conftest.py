from fastapi.testclient import TestClient
from pytest import fixture

from tests.data.user import test_user_a, test_user_b, create_user, delete_user


@fixture(scope="function")
def client(start_up_client: TestClient):
    create_user(test_user_a)
    yield start_up_client
    delete_user(test_user_a)
    delete_user(test_user_b)
