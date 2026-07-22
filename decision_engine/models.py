from dataclasses import dataclass, field


@dataclass
class DecisionAssessment:

    dimension: str

    score: int

    explanation: str



@dataclass
class DecisionProfile:

    action: str

    assessments: list = field(
        default_factory=list
    )

    total_score: float = 0.0
