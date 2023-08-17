from typing import List, Optional

from pydantic import BaseModel, Field

from app.schemas.tasks import TaskSchema


class TodoListSchema(BaseModel):
    name: str = Field(description='todo list name')
    description: Optional[str] = None
    id: int
    tasks: List[TaskSchema] = []

    class Config:
        orm_mode = True
        model_config = {"from_attributes": True, "use_enum_values": True}


class TodoListIn(BaseModel):
    name: str = Field(description='todo list name')
    description: Optional[str] = None
    user_id: int

    class Config:
        orm_mode = True
        model_config = {"from_attributes": True, "use_enum_values": True}
