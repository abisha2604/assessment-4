from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String,Date
from database.db import engine

Base = declarative_base()

class User(Base):
    __tablename__ ='users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    password = Column(String, nullable=False)



class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    due_date = Column(Date, nullable=False)
    priority = Column(String, nullable=False)

Base.metadata.create_all(engine)