from pydantic import BaseModel, EmailStr
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

# ユーザー登録用
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# ユーザー情報（レスポンス用）
class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True

# ログイン用
class UserLogin(BaseModel):
    username: str
    password: str

# トークンレスポンス
class Token(BaseModel):
    access_token: str
    token_type: str
    # ユーザー登録用
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# ユーザー情報（レスポンス用）
class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True

# ログイン用
class UserLogin(BaseModel):
    username: str
    password: str

# トークンレスポンス
class Token(BaseModel):
    access_token: str
    token_type: str