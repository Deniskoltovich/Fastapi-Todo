import secrets
from datetime import datetime, timedelta
from typing import Annotated, Optional, Union

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import (
    HTTPBasic,
    HTTPBasicCredentials,
    OAuth2PasswordBearer,
)
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.repositories.user import UserRepository
from app.services.user import UserService
from config.config import settings
from db.config import async_session

security = HTTPBasic()


class AuthService:
    @staticmethod
    def create_access_token(
        data: dict, expires_delta: Optional[timedelta] = None
    ):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(
                minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
            )
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM
        )
        return encoded_jwt

    @staticmethod
    async def authenticate_user(
        username: str, password: str, db: AsyncSession
    ) -> Union[User, None]:
        user = await UserRepository(db).get_by_username(username)
        if user is None:
            return None
        if not UserService.verify_password(password, user.password):
            return None
        return user

    @staticmethod
    async def get_current_user_from_token(
        token: str = Depends(OAuth2PasswordBearer('auth/token')),
    ):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
            )
            username: str = payload.get("username")
            if username is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        async with async_session() as db:
            user = await UserRepository(db).get_by_username(username)
        if user is None:
            raise credentials_exception
        return user
