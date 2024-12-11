# src/api/user.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
# from typing import Optional

from src.database import get_session

from src.model.user import UserCreate, UserResponse
from src.service import user as curd

router = APIRouter()


@router.get("/{username}", response_model=UserResponse)
def get_user(username: str, session: Session = Depends(get_session)):
    return curd.get_user(session, username=username)


@router.post("", response_model=UserResponse)
def create_user(user_model: UserCreate, session: Session = Depends(get_session)):
    return curd.create_user(session, user_model)
