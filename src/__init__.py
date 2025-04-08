from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.database import create_db
from src.routes.note import note


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db()
    print("Приложение включено")
    yield
    print("Приложение выключено")


def create_app():
    app = FastAPI(lifespan=lifespan)
    app.include_router(note)

    return app