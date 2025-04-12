import bcrypt
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.database import async_session
from src.db.models import User
from sqlalchemy import select, update, delete

from src.schemas.user import UserRegister


class RepositoryUser:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def set_user(self, creds: UserRegister):
        async with async_session() as session:
            user = User(name=creds.name,
                        email=creds.email,
                        password=creds.password)
            session.add(user)
            await session.commit()
            return user.id

    async def get_user_by_name(self, name: str):
        async with async_session() as session:
            user = await session.scalar(select(User).where(User.name == name))
            return user

    async def get_user_by_email(self, email: str):
        async with async_session() as session:
            user = await session.scalar(select(User).where(User.email == email))
            return user

    async def get_login_user(self, name: str, password: str):
        async with async_session() as session:
            user = await session.scalar(select(User).where(User.name == name))
            if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return user
            return None

