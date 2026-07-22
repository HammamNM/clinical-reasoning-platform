from dataclasses import dataclass


@dataclass
class OutcomeEvent:

    event_type: str

    severity_change: int

    description: str
