# src/common/authentication.py

from datetime import datetime, timezone
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError, decode as jwt_decode, encode as jwt_encode
from sqlalchemy.orm import Session
from typing import Any, Optional

from src.common.configuration import JWT_ALGORITHM, JWT_SECRET_KEY
from src.common.exception import Unauthorized, UnprocessableContent
from src.common.password_hashing import verify_password
from src.database import get_session
from src.database.user import User
from src.service.user import get_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def encode_jwt_token(data: dict[str, Any]) -> str:
    payload: dict[str, Any] = {}
    payload.update(data)
    payload["iat"] = datetime.now(timezone.utc)
    return jwt_encode(payload, JWT_SECRET_KEY, JWT_ALGORITHM)


def decode_jwt_token(token: str) -> dict[str, Any]:
    try:
        return jwt_decode(token, JWT_SECRET_KEY, JWT_ALGORITHM)
    except InvalidTokenError as e:
        raise Unauthorized(f"Invalid token - {e}")


def authenticate_user(session: Session, username: str, password: str) -> User:
    user = get_user(session, username=username)
    if verify_password(password, user.password_hash) is True:
        return user

    raise Unauthorized("Invalid username or password")


def get_current_user(
    session: Session = Depends(get_session), token: str = Depends(oauth2_scheme)
):
    payload = decode_jwt_token(token)
    username: Optional[str] = payload.get("sub")
    if not isinstance(username, str):
        raise UnprocessableContent("Could not validate credentials")

    return get_user(session, username=username)
