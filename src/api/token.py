# src/api/token.py

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.common.authentication import encode_jwt_token
from src.database import get_session
from src.model.token import TokenResponse
from src.service.user import authenticate_user

router = APIRouter()


@router.post("", response_model=TokenResponse)
def get_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    user = authenticate_user(session, form_data.username, form_data.password)
    encoded_token = encode_jwt_token({"sub": user.username})
    return TokenResponse(access_token=encoded_token, token_type="Bearer")
