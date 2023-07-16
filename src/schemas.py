from pydantic import BaseModel, EmailStr
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True
