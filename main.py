from fastapi import FastAPI
from src.utils.db import Base, engine
from src.tasks.models import TaskModel
from src.tasks.router import tasks_router
from src.users.router import user_routes


Base.metadata.create_all(engine)
app = FastAPI(title="Task Management API", description="API for managing tasks", version="1.0.0")

app.include_router(tasks_router)
app.include_router(user_routes)