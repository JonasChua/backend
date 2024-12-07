from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from src.common.configuration import DATABASE_URL

engine = create_engine(DATABASE_URL, pool_size=20, max_overflow=10, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass
