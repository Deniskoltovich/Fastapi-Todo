import typing
from typing import Optional

from pydantic import BaseModel, Field

from app.schemas.tasks import TaskSchema


class TodoListSchema(BaseModel):
    name: str = Field(description='todo list name')
    description: Optional[str] = None
    tasks: Optional[typing.List[TaskSchema]] = None

    class Config:
        orm_mode = True
        model_config = {"from_attributes": True, "use_enum_values": True}
