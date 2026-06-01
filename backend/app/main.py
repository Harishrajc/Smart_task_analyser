from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  #allow frontend and backend to communicate
from pydantic import BaseModel #use for request validation(check incoming json data)

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# DATABASE(configuration)
DATABASE_URL = "sqlite:///./task.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(         #create database session(crud operaion uses a session)
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# MODEL
class Task(Base):    #creates task table model
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)

# CREATE TABLE
Base.metadata.create_all(bind=engine)

# REQUEST MODEL(schema)
class TaskCreate(BaseModel):
    title: str

# FASTAPI
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GET TASKS
@app.get("/tasks")
def get_tasks():

    db = SessionLocal()

    tasks = db.query(Task).all()  #get all task from database

    db.close()

    return tasks

# CREATE TASK
@app.post("/tasks")
def create_task(task: TaskCreate):

    db = SessionLocal()

    new_task = Task(title=task.title)

    db.add(new_task)

    db.commit()

    db.refresh(new_task)

    db.close()

    return new_task

# UPDATE TASK
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskCreate):
    db = SessionLocal()

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        db.close()
        return {"error": "Task not found"}

    # UPDATE TITLE
    task.title = updated_task.title

    # SAVE CHANGES
    db.commit()

    # REFRESH
    db.refresh(task)

    db.close()

    return {
        "message": "Task updated",
        "task": task.title
    }

# DELETE TASK
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    db = SessionLocal()

    task = db.query(Task).filter(Task.id == task_id).first()

    if task:
        db.delete(task)
        db.commit()

    db.close()

    return {"message": "Task deleted"}