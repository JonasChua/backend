# tests/data/user.py

from src.common.password_hashing import hash_password
from src.database.user import User
from tests.common.database import get_session


test_user_a = {"username": "username_a", "password": "P@ssw0rd!", "name": "name_a"}
test_user_b = {"username": "username_b", "password": "P@ssw0rd!", "name": "name_b"}


def create_user(user_dict: dict[str, str]) -> User:
    session = get_session()
    db_user = session.query(User).filter(User.username == user_dict["username"]).first()
    if db_user is not None:
        return db_user

    create_user_dict = user_dict.copy()
    create_user_dict["password_hash"] = hash_password(create_user_dict.pop("password"))
    db_user = User(**create_user_dict)
    session.add(db_user)
    session.commit()
    return db_user


def delete_user(user_dict: dict[str, str]) -> None:
    session = get_session()
    db_user = session.query(User).filter(User.username == user_dict["username"]).first()
    if db_user is not None:
        session.delete(db_user)
        session.commit()
