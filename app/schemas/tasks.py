import enum
import typing
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class TaskStatus(str, enum.Enum):
    in_progress = 'In progress'
    done = 'Done'


class TaskSchema(BaseModel):
    name: str = Field(description='task name')
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.in_progress

    class Config:
        orm_mode = True
        model_config = {"from_attributes": True, "use_enum_values": True}
