from pydantic import BaseModel, EmailStr, Field


class UserOut(BaseModel):
    username: str = Field(description='username')
    email: str = Field(description="user email")


class UserIn(UserOut):
    password: str = Field(
        min_length=5, max_length=24, description="user password"
    )
