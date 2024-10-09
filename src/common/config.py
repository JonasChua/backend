import os
from dotenv import load_dotenv
from logging import INFO, basicConfig, getLogger

basicConfig(level=INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = getLogger(__name__)

load_dotenv()

ENVIRONMENT = os.getenv("ENVIRONMENT")
logger.info(f"{ENVIRONMENT=}")

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DATABASE_URL = (
    f"postgresql+psycopg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
logger.info(f"{DATABASE_URL=}")
