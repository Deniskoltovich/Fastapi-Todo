from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.user import User
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def create(self, user_data: dict):
        user = User(**user_data)
        result = await super()._create(user)
        return result

    async def get(self, pk):
        result = await self._get(User, pk)
        return result

    async def get_todo_lists(self, user_id: int):
        result = await self.session.execute(
            select(User)
            .filter_by(id=user_id)
            .order_by(User.id)
            .options(selectinload(User.todo_lists))
        )
        return result.scalars().first().todo_lists

    async def get_by_username(self, username):
        result = await self.session.execute(
            select(User).filter_by(username=username).fetch(count=1)
        )
        return result.scalar()

    async def get_all(self) -> List[User]:
        return await self._get_all(User)

    async def update(self, instance: User, values: dict):
        return await self._update(User, instance, values)
