from dataclasses import dataclass, field
import uuid


@dataclass
class Evidence:

    evidence_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    source: str = ""

    content: str = ""

    supports: list = field(
        default_factory=list
    )

    contradicts: list = field(
        default_factory=list
    )

    strength: float = 1.0
