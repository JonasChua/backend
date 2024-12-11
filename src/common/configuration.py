# src/common/configuration.py

from os import environ
from dotenv import load_dotenv
from logging import getLogger
from logging.config import fileConfig

fileConfig("./logging.conf", disable_existing_loggers=False)
logger = getLogger(__name__)

load_dotenv()

ENVIRONMENT = environ["ENVIRONMENT"]
logger.info(f"{ENVIRONMENT=}")

DB_USERNAME = environ["DB_USERNAME"]
DB_PASSWORD = environ["DB_PASSWORD"]
DB_HOST = environ["DB_HOST"]
DB_PORT = environ["DB_PORT"]
DB_NAME = environ["DB_NAME"]
DATABASE_URL = (
    f"postgresql+psycopg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
logger.info(f"{DB_NAME=}")

JWT_SECRET_KEY = environ["JWT_SECRET_KEY"]
JWT_ALGORITHM = "HS256"
