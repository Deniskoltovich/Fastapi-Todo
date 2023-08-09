from fastapi import Depends, FastAPI, Response

from app.routers.login import login_router
from app.routers.tasks import router as task_router
from app.routers.todo_lists import router as todo_router
from app.routers.users import router as user_router

app = FastAPI()
app.include_router(task_router)
app.include_router(user_router)
app.include_router(login_router)
app.include_router(todo_router)


@app.get('/health')
def health():
    return Response(status_code=200)
