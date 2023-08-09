from typing import Any, List, Union

from fastapi import APIRouter, Depends

from app.models.user import User
from app.schemas.todo_lists import TodoListIn, TodoListSchema
from app.services.auth import AuthService
from app.services.todo_list import TodoListService

router = APIRouter(
    prefix="/todo",
    tags=["ToDo"],
)


@router.get('/')
async def list_todos(
    user: User = Depends(AuthService.get_current_user_from_token),
):
    return await TodoListService.list(user)


@router.get('/{task_id}')
async def get_todo_by_id(
    todo_list_id: int,
    user: User = Depends(AuthService.get_current_user_from_token),
):
    return await TodoListService.get(todo_list_id, user)


@router.post('/', response_model=TodoListIn)
async def create_todo_list(todo_list: TodoListIn):
    return await TodoListService.create(todo_list)


@router.delete('/{task_id}')
async def delete_todo_list(
    task_id: int, user: User = Depends(AuthService.get_current_user_from_token)
):
    return await TodoListService.delete_todo_list(task_id, user)


@router.put('/{task_id}', response_model=TodoListSchema)
async def update_todo_list(
    task_id: int,
    task: TodoListSchema,
    user: User = Depends(AuthService.get_current_user_from_token),
):
    return await TodoListService.update(task_id, task, user)
