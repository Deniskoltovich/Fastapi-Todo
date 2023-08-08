from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Response

from app.models.user import User
from app.permissions import RoleChecker
from app.repositories.user import UserRepository
from app.schemas.users import UserIn, UserOut
from app.services.auth import AuthService
from app.services.user.common import UserService
from app.services.user.creation import CreateUserService
from db.config import async_session

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post('/')
async def create_user(user_data: UserIn) -> UserOut:
    user = await CreateUserService.create_user(user_data.model_dump())
    return user


@router.get('/', response_model=List[UserOut])
async def list_users(permission: Any = Depends(RoleChecker([User.Admin]))):
    return await UserService.list_users()


@router.get('/{user_id}', response_model=UserOut)
async def get_user(
    user_id: int,
    request_user: User = Depends(AuthService.get_current_user_from_token),
):
    if request_user.role != User.Admin and user_id != request_user.id:
        return HTTPException(status_code=403, detail="Operation not permitted")
    return await UserService.get_user(user_id)


@router.post('/{user_id}', response_model=UserOut)
async def update_user(
    user_data: UserOut,
    user_id: int,
    request_user=Depends(AuthService.get_current_user_from_token),
):
    if request_user.role != User.Admin and user_id != request_user.id:
        return HTTPException(status_code=403, detail="Operation not permitted")
    return await UserService.update_user(user_id, user_data)


@router.delete('/{user_id}', response_model=Response)
async def delete_user(
    user_id, permission: Any = Depends(RoleChecker([User.Admin]))
):
    await UserService.delete(user_id)
    return Response("User successfully deleted", status_code=203)
