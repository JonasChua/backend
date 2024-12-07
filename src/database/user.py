# src/database/user.py

from sqlalchemy.orm import Mapped, mapped_column

from src.common.constants import TableName
from src.database.base import Base


class User(Base):
    __tablename__ = TableName.USER

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    name: Mapped[str] = mapped_column()
