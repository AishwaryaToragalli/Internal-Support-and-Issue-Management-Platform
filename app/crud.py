from sqlalchemy.orm import Session

from app import models
from app.schemas import TicketCreate
from app.schemas import TicketUpdate


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
