# src/database/__init__.py

from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.common.configuration import DATABASE_URL
from src.database.base import Base
from src.database.user import User

__all__ = ["Base", "User"]
engine = create_engine(DATABASE_URL, pool_size=20, max_overflow=10, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def initialise_database():
    configuration = Config("./alembic.ini")
    command.upgrade(configuration, "head")


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
