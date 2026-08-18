from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException, Depends
from src.utils.helpers import is_authenticated
from src.users.model import UserModel
from src.utils.db import get_db



def create_task(body : TaskSchema, db : Session=Depends(get_db), user: UserModel=Depends(is_authenticated)):
    data = body.model_dump()
    new_task = TaskModel(title=data['title'], description = data['description'], is_completed=data['is_completed'], user_id = user.id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"status": "Task created successfully...", "data" : new_task}


def get_tasks(db : Session, user: UserModel=Depends(is_authenticated)):
    tasks = db.query(TaskModel).filter(TaskModel.user_id == user.id).all()
    return {"status" : "Tasks retrieved Successfully...", "data" : tasks}


def get_one_task(task_id : int, db : Session, user: UserModel=Depends(is_authenticated)):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail="Task id is Incorrect...")
    if one_task.user_id != user.id:
        raise HTTPException(403, detail="you are not authorized to access this task...")
    
    return {"status" : "Task retrieved Successfully...", "data" : one_task}

def update_task(body: TaskSchema, task_id: int, db: Session, user: UserModel=Depends(is_authenticated)):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail="No task found with this id")
    

    # one_task.title = body.title
    # one_task.description = body.description
    # one_task.is_completed = body.is_completed

    body = body.model_dump()
    for field, value in body.items():
        setattr(one_task, field, value)

    db.add(one_task)
    db.commit()
    db.refresh(one_task)

    return {"status" : "Task updated Successfully....", "data": one_task}


def delete_task(task_id:int, db:Session, user: UserModel=Depends(is_authenticated)):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(404, detail="Task Id is Incorrect")
    if one_task.user_id != user.id:
        raise HTTPException(403, detail = "you are not authorized to delete this task...")
    db.delete(one_task)
    db.commit()
    return{"status": "Task is Delete Successfully..."}