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
    todo_list_id: int

    class Config:
        orm_mode = True


class TodoListSchema(BaseModel):
    name: str = Field(description='todo list name')
    description: Optional[str] = None
    tasks: Optional[typing.List[TaskSchema]] = None

    class Config:
        orm_mode = True
