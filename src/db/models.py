from typing import Annotated

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.db.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]


class User(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))


class Note(Base):
    __tablename__ = "notes"

    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(String(100))
    desc: Mapped[str] = mapped_column(String(1000), nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)