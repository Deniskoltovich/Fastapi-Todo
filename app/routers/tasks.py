from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.tasks import Task
from app.schemas.tasks import TaskSchema

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


# @router.get('/')
# async def get_tasks() -> List[TaskSchema]:
#     result = await session.execute(select(Task))
#     tasks = result.scalars().all()
#
#     task_schemas = [TaskSchema.model_validate(task) for task in tasks]
#
#     return task_schemas
#
# @router.get('/{task_id}')
# async def get_task_by_id() -> TaskSchema:
#     pass
#     # query = select(Task).where(User.id == )
