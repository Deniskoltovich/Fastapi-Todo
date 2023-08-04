import asyncio

from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.user.models import User
from app.user.schemas import UserIn, UserOut
from db.config import get_session

app = FastAPI()


@app.get('/')
def health():
    return "ok"


@app.post('/add')
async def add_user(user: UserIn, session: AsyncSession = Depends(get_session)):
    new_user = User(
        username=user.username, email=user.email, password=user.password
    )
    session.add(new_user)
    try:
        await session.commit()
        return user
    except IntegrityError as ex:
        await session.rollback()
        return f"error:{ex.args}"


@app.get('/users')
async def get_users(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User))
    return result.scalars().all()
