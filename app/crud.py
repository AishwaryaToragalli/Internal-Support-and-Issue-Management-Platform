from sqlalchemy.orm import Session

from app import models
from app.schemas import TicketCreate
from app.schemas import TicketUpdate
from app.auth_schemas import UserCreate
from app.security import hash_password


def create_ticket(
    db: Session,
    ticket_data: TicketCreate,
    priority: str
):
    ticket = models.Ticket(
        title=ticket_data.title,
        description=ticket_data.description,
        priority=priority,
        category=ticket_data.category,
        assigned_to=ticket_data.assigned_to
    )

    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    return ticket


def get_user_by_email(
    db: Session,
    email: str
):
    return (
        db.query(models.User)
        .filter(models.User.email == email)
        .first()
    )


def create_user(
    db: Session,
    user_data: UserCreate
):
    user = models.User(
        full_name=user_data.full_name,
        email=user_data.email,
        password_hash=hash_password(
            user_data.password
        ),
        role=user_data.role
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_ticket(
    db: Session,
    ticket_id: int
):
    return (
        db.query(models.Ticket)
        .filter(models.Ticket.id == ticket_id)
        .first()
    )


def get_tickets(
    db: Session,
    status: str | None = None
):
    query = db.query(models.Ticket)

    if status:
        query = query.filter(
            models.Ticket.status == status
        )

    return query.order_by(
        models.Ticket.created_at.desc()
    ).all()


def update_ticket(
    db: Session,
    ticket_id: int,
    ticket_data: TicketUpdate
):
    ticket = get_ticket(db, ticket_id)

    if not ticket:
        return None

    values = ticket_data.model_dump(
        exclude_unset=True
    )

    for field, value in values.items():
        setattr(ticket, field, value)

    db.commit()
    db.refresh(ticket)

    return ticket
