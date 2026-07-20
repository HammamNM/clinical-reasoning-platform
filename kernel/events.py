from dataclasses import dataclass
from datetime import datetime


@dataclass
class ReasoningEvent:
    event_id: str
    event_type: str
    content: str
    timestamp: str = datetime.utcnow().isoformat()
