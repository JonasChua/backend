# src/service/user.py

from sqlalchemy.orm import Session
# from typing import Optional

from src.database.user import User
from src.model.user import UserCreate


def get_user(session: Session, username: str):
    return session.query(User).filter(User.username == username).one()


def create_user(session: Session, user_model: UserCreate) -> User:
    user = User(**user_model.model_dump(exclude_unset=True))
    session.add(user)
    session.commit()
    return user
