from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from models import Priority

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Priority = Priority.medium
    tag: Optional[str] = None
    due_date: Optional[datetime] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[Priority] = None
    tag: Optional[str] = None
    due_date: Optional[datetime] = None
    is_done: Optional[bool] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    priority: Priority
    tag: Optional[str]
    due_date: Optional[datetime]
    is_done: bool
    created_at: datetime

    class Config:
        from_attributes = True