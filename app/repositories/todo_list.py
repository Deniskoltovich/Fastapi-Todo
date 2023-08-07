from sqlalchemy.ext.asyncio import AsyncSession

from app.models.todo_lists import TodoList
from app.repositories.base import BaseRepository


class TaskRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def create(self, task_data: dict):
        todo_list = TodoList(**task_data)
        result = await super()._create(todo_list)
        return result

    async def get(self, pk):
        result = await self._get(TodoList, pk)
        return result

    async def get_all(self):
        return await self._get_all(TodoList)

    async def update(self, instance: TodoList, values: dict):
        return await self._update(TodoList, instance, values)
