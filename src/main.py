# src/main.py

from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm
from logging import getLogger
from sqlalchemy.orm import Session
from typing import Annotated

from src.api.user import router as user_router
from src.common.authentication import (
    authenticate_user,
    encode_jwt_token,
    get_current_user,
)
from src.database import get_session, initialise_database
from src.database.user import User
from src.model.token import Token
from src.model.user import UserResponse

logger = getLogger(__name__)


@asynccontextmanager
async def lifespan(application: FastAPI):
    try:
        logger.info("Initialising Database")
        initialise_database()
    except Exception as e:
        logger.info(e)
    yield


app = FastAPI(title="Personal API", lifespan=lifespan)


@app.get("/")
def root():
    return {"Info": app.title}


@app.get("/whoami", response_model=UserResponse)
def current_user(user: Annotated[User, Depends(get_current_user)]):
    return user


@app.post("/token", response_model=Token)
def get_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Session = Depends(get_session),
):
    user = authenticate_user(session, form_data.username, form_data.password)
    encoded_token = encode_jwt_token({"sub": user.username})
    return Token(access_token=encoded_token, token_type="Bearer")


app.include_router(user_router, prefix="/user", tags=["user"])
