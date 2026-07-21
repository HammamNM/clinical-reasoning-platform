from dataclasses import dataclass
from datetime import datetime
import uuid


@dataclass
class ReasoningEvent:

    event_id: str
    event_type: str
    content: str
    timestamp: str = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.utcnow().isoformat()


def create_event(event_type, content):

    return ReasoningEvent(
        event_id=str(uuid.uuid4()),
        event_type=event_type,
        content=content
    )
class EventStream:

    def __init__(self):
        self.events = []


    def add(self, event):
        self.events.append(event)


    def get_all(self):
        return self.events
