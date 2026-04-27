from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Task, User
from schemas import TaskCreate, TaskUpdate, TaskResponse
from auth import get_current_user
from typing import List

router = APIRouter(prefix="/tasks", tags=["tasks"])

# タスク一覧取得（自分のタスクのみ）
@router.get("/", response_model=List[TaskResponse])
def get_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # ← 追加
):
    return db.query(Task).filter(Task.user_id == current_user.id).all()

# タスク作成
@router.post("/", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # ← 追加
):
    db_task = Task(**task.dict(), user_id=current_user.id)  # ← user_idを追加
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# タスク更新（自分のタスクのみ）
@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # ← 追加
):
    db_task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == current_user.id  # ← 自分のタスクのみ
    ).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in task.dict(exclude_unset=True).items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task

# タスク削除（自分のタスクのみ）
@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # ← 追加
):
    db_task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == current_user.id  # ← 自分のタスクのみ
    ).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
    return {"message": "Task deleted"}