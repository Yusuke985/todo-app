from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models
from routers import tasks, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS設定（フロントエンドからのアクセスを許可）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Hello, Todo App!"}