from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.tokens import Token
from app.services.auth import AuthService
from config.config import settings
from db.config import async_session

login_router = APIRouter(prefix='/auth', tags=['Auth'])


@login_router.post("/token")
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    access_token = await AuthService.authenticate_user(form_data)
    return {"access_token": access_token, "token_type": "bearer"}
