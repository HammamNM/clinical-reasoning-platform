from dataclasses import dataclass


@dataclass
class DecisionAssessment:

    dimension: str

    score: int

    explanation: str
