# tests/common/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.common.configuration import DATABASE_URL
from src.database.base import Base

TEST_DATABASE_URL = f"{DATABASE_URL}_test"
engine = create_engine(TEST_DATABASE_URL)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_test_session():
    test_session = TestSessionLocal()
    try:
        yield test_session
    finally:
        test_session.close()


def get_session():
    return next(get_test_session())
