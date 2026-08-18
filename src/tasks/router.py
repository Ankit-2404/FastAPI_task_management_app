from fastapi import APIRouter, Depends
from src.tasks import controller
from src.tasks.dtos import TaskSchema
from src.users.model import UserModel
from src.utils.db import get_db
from src.utils.helpers import is_authenticated


tasks_router = APIRouter(prefix="/tasks",)
@tasks_router.post("/create")
def create_task(body : TaskSchema, db = Depends(get_db), user = Depends(is_authenticated)):
  return controller.create_task(body, db, user)

@tasks_router.get("/all_tasks")
def get_tasks(db = Depends(get_db), user: UserModel = Depends(is_authenticated)):
  return controller.get_tasks(db, user)


@tasks_router.get("/one_task/{task_id}")
def get_one_task(task_id : int, db = Depends(get_db), user: UserModel = Depends(is_authenticated)):
  return controller.get_one_task(task_id, db, user)

@tasks_router.put("/update_task/{task_id}")
def update_task(body:TaskSchema, task_id :int, db = Depends(get_db), user: UserModel = Depends(is_authenticated)):
  return controller.update_task(body, task_id, db, user)


@tasks_router.delete("/delete_task/{task_id}")
def delete_task(task_id : int, db=Depends(get_db), user: UserModel = Depends(is_authenticated)):
  return controller.delete_task(task_id,db, user)