from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.errors import CustomException
from src.schemas.note import NoteModel
from src.handlers.note_repository import RepositoryNote, get_db

note = APIRouter()


@note.get("/")
async def root():
    return {"message": "OK"}


@note.post("/notes")
async def add_note(note_model: NoteModel, db: AsyncSession = Depends(get_db)):
    repo = RepositoryNote(db)
    new_note = await repo.set_note(note_model)
    return {"note_id": new_note}


@note.get("/notes", response_model=List[NoteModel])
async def all_notes(db: AsyncSession = Depends(get_db)):
    repo = RepositoryNote(db)
    notes = await repo.get_all_notes()
    return notes


@note.get("/notes/{id}")
async def note_info(id: int, db: AsyncSession = Depends(get_db)):
    repo = RepositoryNote(db)
    one_note = await repo.get_note(id)
    if one_note:
        return one_note
    raise CustomException(detail="Note not found", status_code=404)


@note.put("/notes/edit/title/{id}")
async def new_title(id: int, title: str, db: AsyncSession = Depends(get_db)):
    repo = RepositoryNote(db)
    one_note = await repo.get_note(id)
    if one_note:
        await repo.edit_note_title(id, title)
        return {"message": "ok"}
    raise CustomException(detail="Note not found", status_code=404)


@note.put("/notes/edit/desc/{id}")
async def new_desc(id: int, desc: str, db: AsyncSession = Depends(get_db)):
    repo = RepositoryNote(db)
    one_note = await repo.get_note(id)
    if one_note:
        await repo.edit_note_desc(id, desc)
        return {"message": "ok"}
    raise CustomException(detail="Note not found", status_code=404)


@note.delete("/notes/delete/{id}")
async def remove_note(id: int, db: AsyncSession = Depends(get_db)):
    repo = RepositoryNote(db)
    one_note = await repo.get_note(id)
    if one_note:
        await repo.delete_note(id)
        return {"message": "ok"}
    raise CustomException(detail="Note not found", status_code=404)
