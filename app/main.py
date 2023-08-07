from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.repositories.user import UserRepository
from app.routers.tasks import router as task_router
from app.schemas.users import UserIn
from db.config import async_session

app = FastAPI()
app.include_router(task_router)


@app.get('/')
def health():
    return "ok"


@app.post('/add')
async def add_user(user: UserIn):
    new_user = User(
        username=user.username, email=user.email, password=user.password
    )
    async with async_session() as session:
        session.create(new_user)
        try:
            await session.commit()
            return user
        except IntegrityError as ex:
            await session.rollback()
            return f"error:{ex.args}"


@app.get('/users')
async def get_users():
    async with async_session() as session:
        result = await UserRepository(session).get_all()
    return result
