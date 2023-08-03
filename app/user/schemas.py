from pydantic import BaseModel, EmailStr, Field


class UserOut(BaseModel):
    username: str = Field(description='username')


class UserIn(UserOut):
    email: EmailStr = Field(description="user email")
    password: str = Field(
        min_length=5, max_length=24, description="user password"
    )
