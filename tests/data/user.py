# tests/data/user.py

from src.database.user import User
from tests.common.database import get_session


test_user_a = {"username": "username_a", "name": "name_a"}
test_user_b = {"username": "username_b", "name": "name_b"}


def create_user(user_dict: dict[str, str]) -> User:
    session = get_session()
    db_user = session.query(User).filter(User.username == user_dict["username"]).first()
    if db_user is not None:
        return db_user

    db_user = User(**user_dict)
    session.add(db_user)
    session.commit()
    return db_user


def delete_user(user_dict: dict[str, str]) -> None:
    session = get_session()
    db_user = session.query(User).filter(User.username == user_dict["username"]).first()
    if db_user is not None:
        session.delete(db_user)
        session.commit()
