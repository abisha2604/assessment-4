from pydantic import BaseModel
from datetime import date

class Signup(BaseModel):
    name:str
    email:str
    password:str

class Login(BaseModel):
    email:str
    password:str

class Task(BaseModel):
    title:str
    description:str
    due_date:date
    priority:str



