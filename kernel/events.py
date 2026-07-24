from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict
import uuid


@dataclass(frozen=True)
class ReasoningEvent:

    event_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    event_type: str = ""

    payload: Dict[str, Any] = field(
        default_factory=dict
    )

    source: str = ""

    timestamp: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )



class EventStream:


    def __init__(self):

        self.events = []



    def publish(
        self,
        event: ReasoningEvent
    ):

        if not isinstance(
            event,
            ReasoningEvent
        ):
            raise TypeError(
                "EventStream accepts only ReasoningEvent"
            )


        self.events.append(
            event
        )



    def get_all(
        self
    ):

        return list(
            self.events
        )



    def get_by_type(
        self,
        event_type
    ):

        return [
            event
            for event in self.events
            if event.event_type == event_type
        ]
