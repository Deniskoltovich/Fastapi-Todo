from typing import List

from app.repositories.user import UserRepository
from app.schemas.users import UserOut
from db.config import async_session


class UserService:
    @staticmethod
    async def list_users() -> List[UserOut]:
        async with async_session() as session:
            users = await UserRepository(session).get_all()
        return users

    @staticmethod
    async def get_user(id: int) -> UserOut:
        async with async_session() as session:
            user = await UserRepository(session).get(id)

        return user

    @staticmethod
    async def update_user(id: int, user_data: UserOut):
        async with async_session() as session:
            user = await UserRepository(session).get(id)
            await UserRepository(session).update(
                instance=user, values=user_data.model_dump()
            )
            await session.commit()
        return None

    @staticmethod
    async def delete(user_id):
        async with async_session() as session:
            user = await UserRepository(session).get(user_id)
            await UserRepository(session).delete(user)
            await session.commit()
        return user
