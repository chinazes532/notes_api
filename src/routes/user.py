import bcrypt

from fastapi import APIRouter, Response, Depends, HTTPException
from authx import AuthX, AuthXConfig
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import load_config
from src.schemas.user import UserLogin, UserRegister
from src.handlers.user_repository import RepositoryUser
from src.handlers import get_db
from src.routes.config import security, config

custom_cfg = load_config()

user = APIRouter(
    tags=["Пользователь"]
)


@user.get("/user")
async def user_check():
    return {"message": "ok"}


@user.post("/register")
async def register(creds: UserRegister, response: Response, db: AsyncSession = Depends(get_db)):
    repo = RepositoryUser(db)

    user_by_name = await repo.get_user_by_name(creds.name)
    user_by_email = await repo.get_user_by_email(creds.email)

    if user_by_name or user_by_email:
        raise HTTPException(detail="User already exists", status_code=400)

    hashed_password = bcrypt.hashpw(creds.password.encode('utf-8'), bcrypt.gensalt())
    creds.password = hashed_password.decode('utf-8')

    user_id = await repo.set_user(creds)

    token = security.create_access_token(uid=str(user_id))
    response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)

    return {"message": "User registered successfully",
            "access_token": token}


@user.post("/login")
async def login(creds: UserLogin, response: Response, db: AsyncSession = Depends(get_db)):
    repo = RepositoryUser(db)

    user_login = await repo.get_login_user(creds.name, creds.password)

    if user_login:
        token = security.create_access_token(uid=str(user_login.id))
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {"message": "User login successfully",
                "access_token": token}
    raise HTTPException(detail="Auth error", status_code=401)