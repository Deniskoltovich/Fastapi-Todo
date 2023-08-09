from fastapi import HTTPException

from app.models.tasks import Task
from app.models.user import User
from app.repositories.task import TaskRepository
from app.schemas.tasks import TaskSchema, TaskSchemaIn
from db.config import async_session


class TaskService:
    @staticmethod
    async def list_tasks(user: User):
        async with async_session() as session:
            if user.role == user.ADMIN:
                result = await TaskRepository(session).get_all()
            else:
                result = await TaskRepository(session).get_tasks_for_user(
                    user.id
                )
        return result

    @staticmethod
    async def create(task: TaskSchemaIn):
        async with async_session() as session:
            task = await TaskRepository(session).create(task.model_dump())
            await session.commit()
        return task

    @staticmethod
    async def get_task(task_id: int, user: User):
        async with async_session() as session:
            task = await TaskRepository(session).get(task_id)
        if user.role == user.USER and task.todo_list not in user.todo_lists:
            raise HTTPException(status_code=403, detail='permission denied')
        return task

    @staticmethod
    async def delete_task(id: int, user: User):
        async with async_session() as session:
            task = await TaskService.get_task(id, user)
            await TaskRepository(session).delete(task)
            await session.commit()

        return task

    @staticmethod
    async def update(id: int, updated_task: TaskSchema, user: User):
        async with async_session() as session:
            task = await TaskService.get_task(id, user)
            result = await TaskRepository(session).update(
                task, updated_task.model_dump()
            )
            await session.commit()
        return result

    @staticmethod
    async def complete_task(id: int, user: User):
        async with async_session() as session:
            task = await TaskService.get_task(id, user)
            task.status = Task.DONE
            session.add(task)
            await session.commit()

        return task
