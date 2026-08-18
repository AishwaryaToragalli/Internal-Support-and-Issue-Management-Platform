from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class TicketCreate(BaseModel):
    title: str = Field(
        min_length=5,
        max_length=200
    )
    description: str = Field(
        min_length=10
    )
    priority: str = "medium"
    category: str = "general"
    assigned_to: Optional[str] = None


class TicketUpdate(BaseModel):
    status: Optional[str] = None
    priority: Optional[str] = None
    assigned_to: Optional[str] = None
    resolution_notes: Optional[str] = None


class TicketResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: str
    category: str
    status: str
    assigned_to: Optional[str]
    resolution_notes: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True
