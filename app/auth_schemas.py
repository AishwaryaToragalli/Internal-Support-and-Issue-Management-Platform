from datetime import datetime

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


class UserCreate(BaseModel):
    full_name: str = Field(
        min_length=2,
        max_length=100
    )
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=128
    )
    role: str = "employee"


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    role: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: int | None = None
