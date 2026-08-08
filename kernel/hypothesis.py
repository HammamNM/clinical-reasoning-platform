from dataclasses import dataclass, field


@dataclass
class Hypothesis:

    name: str

    confidence: float = 0.50

    status: str = "ACTIVE"

    created_by: str = None

    supporting_evidence: list = field(
        default_factory=list
    )

    contradicting_evidence: list = field(
        default_factory=list
    )

    confidence_history: list = field(
        default_factory=list
    )
