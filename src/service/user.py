# src/service/user.py

from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Optional

from src.common.exception import Conflict, NotFound
from src.common.password_hashing import hash_password
from src.database.user import User
from src.model.user import UserCreate

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
