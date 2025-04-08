from sqlalchemy.ext.asyncio import AsyncSession

from src.db.database import async_session
from src.db.models import Note
from sqlalchemy import select, update, delete

from src.schemas.note import NoteModel


async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session


class RepositoryNote:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def set_note(self, note_model: NoteModel):
        async with async_session() as session:
            note = Note(title=note_model.title,
                        desc=note_model.desc)
            session.add(note)
            await session.commit()
            return note.id

    async def get_all_notes(self):
        async with async_session() as session:
            notes = await session.scalars(select(Note))
            return notes

    async def get_note(self, id):
        async with async_session() as session:
            note = await session.scalar(select(Note).where(Note.id == id))
            return note

    async def edit_note_title(self, id, title):
        async with async_session() as session:
            await session.execute(update(Note).where(Note.id == id).values(title=title))
            await session.commit()

    async def edit_note_desc(self, id, desc):
        async with async_session() as session:
            await session.execute(update(Note).where(Note.id == id).values(desc=desc))
            await session.commit()

    async def delete_note(self, id):
        async with async_session() as session:
            await session.execute(delete(Note).where(Note.id == id))
            await session.commit()



