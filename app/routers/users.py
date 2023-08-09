from typing import Any, List, Optional, Union

from fastapi import APIRouter, Depends, HTTPException, Response

from app.models.user import User
from app.permissions import RoleChecker
from app.schemas.users import UserIn, UserOut
from app.services.auth import AuthService
from app.services.user.common import UserService
from app.services.user.creation import CreateUserService

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post('/')
async def create_user(user_data: UserIn) -> UserOut:
    user = await CreateUserService.create_user(user_data.model_dump())
    return user


@router.get('/', response_model=List[UserOut])
async def list_users(permission: Any = Depends(RoleChecker([User.ADMIN]))):
    return await UserService.list_users()


@router.get('/{user_id}', response_model=UserOut)
async def get_user(
    user_id: int,
    request_user: User = Depends(AuthService.get_current_user_from_token),
):
    if request_user.role != User.ADMIN and user_id != request_user.id:
        raise HTTPException(status_code=403, detail="Operation not permitted")
    return await UserService.get_user(user_id)


@router.put('/{user_id}', response_model=Any)
async def update_user(
    user_data: UserOut,
    user_id: int,
    request_user=Depends(AuthService.get_current_user_from_token),
):
    if request_user.role == User.USER and user_id != request_user.id:

        raise HTTPException(status_code=403, detail="Operation not permitted")
    await UserService.update_user(user_id, user_data)
    return Response("User successfully updated", status_code=201)


@router.delete('/{user_id}')
async def delete_user(
    user_id, permission: Any = Depends(RoleChecker([User.ADMIN]))
):
    await UserService.delete(user_id)
    return Response("User successfully deleted", status_code=203)
