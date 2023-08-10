import enum
import typing
from typing import Optional

from pydantic import BaseModel, Field


class TaskStatus(str, enum.Enum):
    IN_PROGRESS = 'in_progress'
    DONE = 'done'


class TaskSchema(BaseModel):
    name: str = Field(description='task name')
    description: Optional[str] = None
    status: Optional[TaskStatus]

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        model_config = {"from_attributes": True, "use_enum_values": True}


class TaskSchemaIn(BaseModel):
    name: str = Field(description='task name')
    description: Optional[str] = None
    status: Optional[TaskStatus] = TaskStatus.IN_PROGRESS
    todo_list_id: int

    class Config:
        orm_mode = True
        model_config = {"from_attributes": True, "use_enum_values": True}
