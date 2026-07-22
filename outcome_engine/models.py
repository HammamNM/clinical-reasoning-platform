from dataclasses import dataclass


@dataclass
class PatientOutcome:

    status: str

    severity: int

    description: str
