from contextlib import asynccontextmanager
from logging import getLogger
from fastapi import FastAPI

from src.common.utils import init_db

logger = getLogger()


@asynccontextmanager
async def lifespan(application: FastAPI):
    try:
        logger.info("Initialising DB")
        init_db()
    except Exception as e:
        logger.info(e)
    yield


app = FastAPI(title="Personal API", lifespan=lifespan)


@app.get("/")
async def root():
    return {"Info": "Personal API"}
