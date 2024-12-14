# src/api/user.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
# from typing import Optional

from src.common.authentication import current_user
from src.database import get_session

from src.database.user import User
from src.model.user import UserCreate, UserResponse, UserUpdate
from src.service import user as curd

router = APIRouter()


@router.get("/{username}", response_model=UserResponse)
def get_user(username: str, session: Session = Depends(get_session)):
    return curd.get_user(session, username=username)


@router.get("/usernames/")
def get_usernames(session: Session = Depends(get_session)):
    return curd.get_usernames(session)


@router.get("/whoami/", response_model=UserResponse)
def get_current_user(user: User = Depends(current_user)):
    return user


@router.post("", response_model=UserResponse)
def create_user(user_model: UserCreate, session: Session = Depends(get_session)):
    return curd.create_user(session, user_model)


@router.patch("", response_model=UserResponse)
def update_user(
    user_model: UserUpdate,
    user: User = Depends(current_user),
    session: Session = Depends(get_session),
):
    return curd.update_user(session, user.username, user_model)
