from dataclasses import dataclass
from enum import Enum


class PrimitiveType(Enum):

    OBSERVATION = "OBSERVATION"

    INVESTIGATION = "INVESTIGATION"

    HYPOTHESIS = "HYPOTHESIS"

    DECISION = "DECISION"

    OUTCOME = "OUTCOME"



@dataclass
class ReasoningUnit:

    id: str

    primitive: PrimitiveType

    content: str
