# src/service/user.py

from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Optional

from src.common.exception import Conflict, NotFound, Unauthorized
from src.common.password_hashing import hash_password, verify_password
from src.database.user import User
from src.model.user import UserCreate, UserUpdate

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_user(
    session: Session, id: Optional[int] = None, username: Optional[str] = None
) -> User:
    if id is not None:
        user = session.query(User).filter(User.id == id).first()
    elif username is not None:
        user = session.query(User).filter(User.username == username).first()
    else:
        user = None

    if user is not None:
        return user

    raise NotFound(f"User {id or username} not found")


def get_usernames(session: Session) -> list[str]:
    return [user[0] for user in session.query(User.username).all()]


def create_user(session: Session, user_model: UserCreate) -> User:
    try:
        get_user(session, username=user_model.username)
        raise Conflict(f"User {user_model.username} already exists")
    except NotFound as e:
        if "User" not in e.message:
            raise e

    user = User(
        **user_model.model_dump(exclude={"password"}, exclude_unset=True),
        password_hash=hash_password(user_model.password),
    )
    session.add(user)
    session.commit()
    return user


def update_username(session: Session, user: User, new_username: str) -> User:
    if user.username == new_username:
        return user

    try:
        get_user(session, username=new_username)
        raise Conflict("Username has been taken")
    except NotFound as e:
        if "User" not in e.message:
            raise e

    user.username = new_username
    session.commit()
    return user


def update_user(session: Session, username: str, user_model: UserUpdate) -> User:
    user = get_user(session, username=username)
    if user_model.username is not None:
        update_username(session, user, user_model.username)

    if user_model.password is not None:
        user.password_hash = hash_password(user_model.password)

    update_fields = user_model.model_dump(
        exclude={"username", "password"}, exclude_unset=True
    )
    for key, value in update_fields:
        setattr(user, key, value)

    session.commit()
    return user


def authenticate_user(session: Session, username: str, password: str) -> User:
    user = get_user(session, username=username)
    valid_password, updated_password_hash = verify_password(
        password, user.password_hash
    )
    if valid_password is False:
        raise Unauthorized("Invalid username or password")

    if updated_password_hash is not None:
        user.password_hash = updated_password_hash
        session.commit()

    return user
