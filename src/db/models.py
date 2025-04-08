from typing import Annotated

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.db.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]


class Note(Base):
    __tablename__ = "notes"

    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(String(100))
    desc: Mapped[str] = mapped_column(String(1000), nullable=True)