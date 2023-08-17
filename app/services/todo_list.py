from fastapi import HTTPException

from app.models.tasks import Task
from app.models.user import User
from app.repositories.todo_list import TodoListRepository
from app.repositories.user import UserRepository
from app.schemas.todo_lists import TodoListIn, TodoListSchema
from db.config import async_session


class TodoListService:
    @staticmethod
    async def list(user: User):
        async with async_session() as session:
            if user.role == user.ADMIN:
                result = await TodoListRepository(session).get_all()
            else:
                result = await UserRepository(session).get_todo_lists(user.id)
        return result

    @staticmethod
    async def create(todo_list: TodoListIn):
        async with async_session() as session:
            todo_list = await TodoListRepository(session).create(
                todo_list.model_dump()
            )
            await session.commit()
        return todo_list

    @staticmethod
    async def get(list_id: int, user: User):
        async with async_session() as session:
            todo_list = await TodoListRepository(session).get(list_id)

        if user.role == user.USER and todo_list not in user.todo_lists:
            raise HTTPException(status_code=403, detail='permission denied')
        return todo_list

    @staticmethod
    async def delete_todo_list(id: int, user: User):
        async with async_session() as session:
            todo_list = await TodoListService.get(id, user)
            await TodoListRepository(session).delete(todo_list)
            await session.commit()

        return todo_list

    @staticmethod
    async def update(id: int, updated_task: TodoListSchema, user: User):
        async with async_session() as session:
            todo_list = await TodoListService.get(id, user)
            result = await TodoListRepository(session).update(
                todo_list, updated_task.model_dump()
            )
            await session.commit()
        return result
