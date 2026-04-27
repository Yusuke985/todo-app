from fastapi import FastAPI
from database import engine
import models
from routers import tasks, auth  # ← authを追加

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tasks.router)
app.include_router(auth.router)  # ← この行を追加

@app.get("/")
def read_root():
    return {"message": "Hello, Todo App!"}