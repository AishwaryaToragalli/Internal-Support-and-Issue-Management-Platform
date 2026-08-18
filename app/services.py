class TicketService:
    VALID_PRIORITIES = {
        "low",
        "medium",
        "high",
        "critical"
    }

    VALID_STATUSES = {
        "open",
        "in_progress",
        "resolved",
        "closed"
    }

    def validate_priority(self, priority: str) -> str:
        priority = priority.lower()

        if priority not in self.VALID_PRIORITIES:
            raise ValueError(
                "Invalid priority value"
            )

        return priority

    def validate_status(self, status: str) -> str:
        status = status.lower()

        if status not in self.VALID_STATUSES:
            raise ValueError(
                "Invalid status value"
            )

        return status

    def calculate_priority(
        self,
        description: str
    ) -> str:
        urgent_words = {
            "security",
            "outage",
            "payment",
            "data loss"
        }

        description = description.lower()

        for word in urgent_words:
            if word in description:
                return "high"

        return "medium"
