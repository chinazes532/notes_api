from fastapi import FastAPI
from contextlib import asynccontextmanager

from starlette.middleware.cors import CORSMiddleware

from src.db.database import create_db
from src.routes.note import note
from src.routes.user import user


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db()
    print("Приложение включено")
    yield
    print("Приложение выключено")


def create_app():
    app = FastAPI(lifespan=lifespan)
    app.include_router(note)
    app.include_router(user)

    return app
