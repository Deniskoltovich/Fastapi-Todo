from sqlalchemy.ext.asyncio import AsyncSession

from app.models.tasks import Task
from app.repositories.base import BaseRepository


class TaskRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def create(self, task_data: dict):
        task = Task(**task_data)
        result = await super()._create(task)
        return result

    async def get(self, pk):
        result = await self._get(Task, pk)
        return result

    async def get_all(self):
        return await self._get_all(Task)

    async def update(self, instance: Task, values: dict):
        return await self._update(Task, instance, values)
