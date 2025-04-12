from sqlalchemy.ext.asyncio import AsyncSession
from src.db.database import async_session


async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session
