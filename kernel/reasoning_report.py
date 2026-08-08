from dataclasses import dataclass, field


@dataclass
class HypothesisReport:

    name: str

    confidence: float

    status: str

    supporting_evidence: list = field(
        default_factory=list
    )

    contradicting_evidence: list = field(
        default_factory=list
    )

    confidence_history: list = field(
        default_factory=list
    )


@dataclass
class ReasoningReport:

    session_id: str

    hypotheses: list = field(
        default_factory=list
    )

    confirmed_hypotheses: list = field(
        default_factory=list
    )

    rejected_hypotheses: list = field(
        default_factory=list
    )

    reasoning_nodes: list = field(
        default_factory=list
    )

    reasoning_edges: list = field(
        default_factory=list
    )

    reasoning_path: list = field(
        default_factory=list
    )

    evidence: list = field(
        default_factory=list
    )
