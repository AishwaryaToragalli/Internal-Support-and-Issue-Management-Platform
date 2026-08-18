import pytest

from app.services import TicketService


def test_payment_issue_gets_high_priority():
    service = TicketService()

    priority = service.calculate_priority(
        "Payment service failure"
    )

    assert priority == "high"


def test_invalid_status_raises_error():
    service = TicketService()

    with pytest.raises(ValueError):
        service.validate_status("invalid")
