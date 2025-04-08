from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from src.config import load_config

config = load_config()

engine = create_async_engine(url=config.db.database_url,
                             echo=True)

async_session = async_sessionmaker(engine,
                                   expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
    pass


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)