from pydantic import BaseModel, EmailStr, Field


class UserOut(BaseModel):
    username: str = Field(description='username')
    email: str = Field(description="user email")

    class Config:
        orm_mode = True
        model_config = {"from_attributes": True, "use_enum_values": True}


class UserIn(UserOut):
    email: str = Field(description="user email")
    password: str = Field(
        min_length=5, max_length=24, description="user password"
    )

    class Config:
        orm_mode = True
        model_config = {"from_attributes": True, "use_enum_values": True}
