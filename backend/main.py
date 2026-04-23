from fastapi import FastAPI
from database import engine
import models
from routers import tasks

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "Hello, Todo App!"}