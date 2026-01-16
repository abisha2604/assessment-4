from fastapi import APIRouter,Depends
from database.get_db import get_db
from services.user_service import user_signup,user_login,create_task,view_task,update_task,delete_task
from models.schema import Signup,Login,Task
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
auth = OAuth2PasswordBearer(tokenUrl="login")

@router.post("/signup")
def signup(data:Signup, db:Session=Depends(get_db)):
    return user_signup(db,data.name, data.email, data.password)

@router.post("/login")
def login(data:Login, db:Session=Depends(get_db),token:str=Depends(auth)):
    return user_login(db, data.email, data.password)

@router.post("/create-task")
def task(data:Task, db:Session=Depends(get_db),token:str=Depends(auth)):
    return create_task(db, data.title, data.description, data.due_date, data.priority)

@router.get("/get-task")
def get_task(data:Task, db:Session=Depends(get_db), token:str=Depends(auth)):
    return view_task(db)

@router.put("/tasks/{task_id}")
def put_task(task_id:int, data:Task, db:Session=Depends(get_db), token:str=Depends(auth)):
    return update_task(db,task_id,data.title, data.description, data.due_date, data.priority)

@router.delete("/delete/{task_id}")
def del_task(task_id:int, db:Session=Depends(get_db), token:str=Depends(auth)):
    return delete_task(db,task_id)






