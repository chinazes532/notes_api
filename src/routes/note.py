from typing import List

from fastapi import APIRouter, Depends, HTTPException

from src.errors import CustomException
from src.schemas.note import NoteModel
from src.schemas.pagination import PaginationDep
from src.handlers.note_repository import RepositoryNote
from src.db.database import SessionDep
from src.routes.config import security

note = APIRouter(
    tags=["Заметки"]
)


@note.get("/", dependencies=[Depends(security.access_token_required)])
async def root():
    return {"message": "OK"}


@note.post("/notes", dependencies=[Depends(security.access_token_required)])
async def add_note(note_model: NoteModel, session: SessionDep):
    try:
        repo = RepositoryNote(session)
        new_note = await repo.set_note(note_model)
        return {"note_id": new_note}
    except KeyError as e:
        raise HTTPException(detail=f"Missing cookie: {str(e)}", status_code=400)
    except Exception as e:
        raise HTTPException(detail=f"An error occurred: {str(e)}", status_code=500)


@note.get("/notes/{user_id}", response_model=List[NoteModel], dependencies=[Depends(security.access_token_required)])
async def all_notes(user_id: int, session: SessionDep, pagination: PaginationDep):
    repo = RepositoryNote(session)
    notes = await repo.get_all_notes_by_user_id(user_id, pagination)
    return notes


@note.get("/notes/{id}")
async def note_info(id: int, session: SessionDep):
    repo = RepositoryNote(session)
    one_note = await repo.get_note(id)
    if one_note:
        return one_note
    raise CustomException(detail="Note not found", status_code=404)


@note.put("/notes/edit/title/{id}", dependencies=[Depends(security.access_token_required)])
async def new_title(id: int, title: str, session: SessionDep):
    repo = RepositoryNote(session)
    one_note = await repo.get_note(id)
    if one_note:
        await repo.edit_note_title(id, title)
        return {"message": "ok"}
    raise CustomException(detail="Note not found", status_code=404)


@note.put("/notes/edit/desc/{id}", dependencies=[Depends(security.access_token_required)])
async def new_desc(id: int, desc: str, session: SessionDep):
    repo = RepositoryNote(session)
    one_note = await repo.get_note(id)
    if one_note:
        await repo.edit_note_desc(id, desc)
        return {"message": "ok"}
    raise CustomException(detail="Note not found", status_code=404)


@note.delete("/notes/delete/{id}", dependencies=[Depends(security.access_token_required)])
async def remove_note(id: int, session: SessionDep):
    repo = RepositoryNote(session)

    one_note = await repo.get_note(id)
    if one_note:
        await repo.delete_note(id)
        return {"message": "ok"}
    raise CustomException(detail="Note not found", status_code=404)
