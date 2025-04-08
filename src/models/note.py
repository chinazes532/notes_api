from pydantic import BaseModel
from typing import Optional


class NoteModel(BaseModel):
    title: str
    desc: Optional[str] = None
