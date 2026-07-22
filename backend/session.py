from decision_engine.models import DecisionProfile
from outcome_engine.models import PatientOutcome
from dataclasses import dataclass, field
from datetime import datetime
import uuid

from simulation.clock import SimulationClock
from simulation.state import SimulationState
from kernel.events import EventStream


@dataclass
class ClinicalSession:

    decision_history: list = field(
    default_factory=list
    )
    
    session_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    student_id: str = ""

    scenario_id: str = ""

    state: SimulationState = field(default_factory=SimulationState)

    event_stream: EventStream = field(default_factory=EventStream)

    clock: SimulationClock = field(default_factory=SimulationClock)

outcome: PatientOutcome = field(
    default_factory=lambda: PatientOutcome(
        status="STABLE",
        severity=0,
        description="Initial patient state"
    )
)

finished: bool = False
