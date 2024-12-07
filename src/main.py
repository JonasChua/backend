from contextlib import asynccontextmanager
from logging import getLogger
from fastapi import FastAPI

from src.database import initialise_database

logger = getLogger()


@asynccontextmanager
async def lifespan(application: FastAPI):
    try:
        logger.info("Initialising DB")
        initialise_database()
    except Exception as e:
        logger.info(e)
    yield


app = FastAPI(title="Personal API", lifespan=lifespan)


@app.get("/")
def root():
    return {"Info": "Personal API"}
