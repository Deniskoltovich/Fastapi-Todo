from passlib.context import CryptContext

from app.repositories.user import UserRepository
from db.config import async_session

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)

    @staticmethod
    async def create_user(user_data: dict):
        password = user_data.pop('password')
        user_data['password'] = UserService.get_password_hash(password)
        async with async_session() as session:
            user = await UserRepository(session).create(user_data)
            await session.commit()

        return user
