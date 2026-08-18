from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from app.database import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String(200),
        nullable=False
    )

    description = Column(
        Text,
        nullable=False
    )

    priority = Column(
        String(20),
        default="medium",
        nullable=False
    )

    category = Column(
        String(50),
        default="general",
        nullable=False
    )

    status = Column(
        String(20),
        default="open",
        nullable=False
    )

    assigned_to = Column(
        String(100),
        nullable=True
    )

    resolution_notes = Column(
        Text,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )
