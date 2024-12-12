# src/main.py

from contextlib import asynccontextmanager
from fastapi import FastAPI
from logging import getLogger

from src.api.user import router as user_router
from src.api.token import router as token_router
from src.database import initialise_database
from src.model.common import MessageResponse

logger = getLogger(__name__)


@asynccontextmanager
async def lifespan(application: FastAPI):
    try:
        logger.info("Initialising Database")
        initialise_database()
    except Exception as e:
        logger.error(e)
    yield


app = FastAPI(title="Personal API", lifespan=lifespan)


@app.get("/", response_model=MessageResponse)
def root():
    return MessageResponse(message=f"{app.title} - {app.version}")


app.include_router(token_router, prefix="/token", tags=["token"])
app.include_router(user_router, prefix="/user", tags=["user"])
