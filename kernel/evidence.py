from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict


@dataclass
class Evidence:

    evidence_id: str

    evidence_type: str

    source: str

    content: Dict[str, Any]

    timestamp: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )
