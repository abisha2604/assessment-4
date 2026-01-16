from fastapi import Depends
from sqlalchemy.orm import Session
from database.get_db import get_db
from models.user_schema import User,Task
from auth.auth import create_token


def user_signup(db:Session,name:str, email:str, password:str):

    data = User(name=name,
                email=email, 
                password=password) 

    db.add(data)
    db.commit()
    db.refresh(data)
    return {"messgaes":"Sign up successfull"}

def user_login(db:Session,email:str, password:str):

    data = db.query(User).filter(User.email==email).first()

    if data.password != password:
        return {"error": "Invalid password"}
    token = create_token(data={"sub":data.email,"user_id":data.id})
    return {"message": "Login successful","token":token}

def create_task(db:Session, title=str, description=str, due_date=str, priority=str):

    data = Task(title=title,
                description=description,
                due_date=due_date,
                priority=priority)

    db.add(data)
    db.commit()
    db.refresh(data)
    return{"message":"Task added successfully"} 
def view_task(db:Session):
    data = db.query(Task).order_by(Task.priority).all()
    return data

def update_task(db:Session,task_id:int, title=str, description=str, due_date=str, priority=str):
    data =  db.query(Task).filter(Task.id == task_id).first()
    if data:
        data.title = title
        data.description = description
        data.due_date = due_date
        data.priority = priority

    db.commit()
        
    return {"messages":"Updated Successfully"}

def delete_task(db:Session,task_id:int):

    data = db.query(Task).filter(Task.id == task_id).first()
    db.delete(data)
    db.commit()

    return{"message":"Deleted Successfully"}






    
                