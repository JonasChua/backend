from alembic import command
from alembic.config import Config
from src.model import SessionLocal


def init_db():
    alembic_cfg = Config("./alembic.ini")
    command.upgrade(alembic_cfg, "head")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
