from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.database import get_db
from app.schemas import TicketCreate
from app.schemas import TicketResponse
from app.schemas import TicketUpdate
from app.services import TicketService

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)

ticket_service = TicketService()


@router.post(
    "/",
    response_model=TicketResponse,
    status_code=201
)
def create_ticket(
    ticket_data: TicketCreate,
    db: Session = Depends(get_db)
):
    priority = ticket_data.priority

    if priority == "medium":
        priority = ticket_service.calculate_priority(
            ticket_data.description
        )

    try:
        priority = ticket_service.validate_priority(
            priority
        )
    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        ) from error

    return crud.create_ticket(
        db,
        ticket_data,
        priority
    )


@router.get(
    "/",
    response_model=list[TicketResponse]
)
def list_tickets(
    status: str | None = None,
    db: Session = Depends(get_db)
):
    if status:
        try:
            ticket_service.validate_status(status)
        except ValueError as error:
            raise HTTPException(
                status_code=400,
                detail=str(error)
            ) from error

    return crud.get_tickets(db, status)


@router.get(
    "/{ticket_id}",
    response_model=TicketResponse
)
def get_ticket(
    ticket_id: int,
    db: Session = Depends(get_db)
):
    ticket = crud.get_ticket(db, ticket_id)

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return ticket


@router.patch(
    "/{ticket_id}",
    response_model=TicketResponse
)
def update_ticket(
    ticket_id: int,
    ticket_data: TicketUpdate,
    db: Session = Depends(get_db)
):
    if ticket_data.status:
        try:
            ticket_service.validate_status(
                ticket_data.status
            )
        except ValueError as error:
            raise HTTPException(
                status_code=400,
                detail=str(error)
            ) from error

    ticket = crud.update_ticket(
        db,
        ticket_id,
        ticket_data
    )

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return ticket
