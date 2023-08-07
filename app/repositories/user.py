from sqlalchemy.ext.asyncio import AsyncSession

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

    async def get_all(self):
        return await self._get_all(User)

    async def update(self, instance: User, values: dict):
        return await self._update(User, instance, values)
