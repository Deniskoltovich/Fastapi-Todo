from fastapi import APIRouter

from app.api.v1.routers.login import login_router
from app.api.v1.routers.tasks import router as task_router
from app.api.v1.routers.todo_lists import router as todo_router
from app.api.v1.routers.users import router as user_router

router = APIRouter(prefix="/v1")

router.include_router(task_router)
router.include_router(user_router)
router.include_router(login_router)
router.include_router(todo_router)
