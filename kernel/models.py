from dataclasses import dataclass
from enum import Enum


from kernel.provenance import (
    ProvenanceRecord
)


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

    provenance: ProvenanceRecord | None = None
