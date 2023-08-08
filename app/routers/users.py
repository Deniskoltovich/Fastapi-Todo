from typing import List

from fastapi import APIRouter, Depends

from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.users import UserIn, UserOut
from app.services.auth import AuthService
from app.services.user import UserService
from db.config import async_session

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post('/')
async def create_user(user_data: UserIn) -> UserOut:
    user = await UserService.create_user(user_data.model_dump())
    return user


@router.get('/', response_model=List[UserOut])
async def get_users(
    user: User = Depends(AuthService.get_current_user_from_token),
):
    async with async_session() as session:
        users = await UserRepository(session).get_all()
    return users


# @router.post('/{user_id}')
# async def update_user(
#     user_id: int, request_user=Depends(
#     AuthService.get_current_user_from_token
#     )
# ):
#     if user_id != request_user.id:
#         return "inavlid"
#     async with async_session() as session:
#         users = await UserRepository(session).update()
#     return users
