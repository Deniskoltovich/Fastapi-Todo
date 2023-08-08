from app.repositories.user import UserRepository
from app.services.user.password_hasher import PasswordService
from db.config import async_session


class CreateUserService:
    @staticmethod
    async def create_user(user_data: dict):
        password = user_data.pop('password')
        user_data['password'] = PasswordService.get_password_hash(password)
        async with async_session() as session:
            user = await UserRepository(session).create(user_data)
            await session.commit()

        return user
