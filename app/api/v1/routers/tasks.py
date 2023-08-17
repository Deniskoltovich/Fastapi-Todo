from typing import List

from fastapi import APIRouter, Depends

from app.models.user import User
from app.schemas.tasks import TaskSchema, TaskSchemaIn
from app.services.auth import AuthService
from app.services.task import TaskService

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


@router.get('/', response_model=List[TaskSchema])
async def get_tasks(
    user: User = Depends(AuthService.get_current_user_from_token),
):
    tasks = await TaskService.list_tasks(user)
    return tasks


@router.get('/{task_id}', response_model=TaskSchema)
async def get_task_by_id(
    task_id: int, user: User = Depends(AuthService.get_current_user_from_token)
):
    return await TaskService.get_task(task_id, user)


@router.post('/', response_model=TaskSchema)
async def create_task(task: TaskSchemaIn):
    return await TaskService.create(task)


@router.delete('/{task_id}')
async def delete_task(
    task_id: int, user: User = Depends(AuthService.get_current_user_from_token)
):
    return await TaskService.delete_task(task_id, user)


@router.put('/{task_id}', response_model=TaskSchema)
async def update_task(
    task_id: int,
    task: TaskSchema,
    user: User = Depends(AuthService.get_current_user_from_token),
):
    return await TaskService.update(task_id, task, user)


@router.get('/{task_id}/done', response_model=TaskSchema)
async def complete_task(
    task_id: int, user=Depends(AuthService.get_current_user_from_token)
):
    return await TaskService.complete_task(task_id, user)
