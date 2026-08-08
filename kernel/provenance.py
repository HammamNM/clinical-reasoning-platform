from dataclasses import dataclass, field
from datetime import datetime
import uuid



@dataclass
class ProvenanceRecord:


    id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )


    source: str = ""


    event_type: str = ""


    timestamp: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )


    metadata: dict = field(
        default_factory=dict
    )
