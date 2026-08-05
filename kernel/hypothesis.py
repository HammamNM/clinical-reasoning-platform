from dataclasses import dataclass, field


@dataclass
class Hypothesis:

    name: str

    confidence: float = 0.0

    status: str = "ACTIVE"

    supporting_evidence: list = field(
        default_factory=list
    )

    contradicting_evidence: list = field(
        default_factory=list
    )

    confidence_history: list = field(
        default_factory=list
    )

    created_by: str | None = None

    last_updated: str | None = None
