from dataclasses import dataclass, field
from datetime import datetime
import uuid

from simulation.clock import SimulationClock
from simulation.state import SimulationState
from kernel.events import EventStream


@dataclass
class ClinicalSession:

    session_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    student_id: str = ""

    scenario_id: str = ""

    state: SimulationState = field(default_factory=SimulationState)

    event_stream: EventStream = field(default_factory=EventStream)

    clock: SimulationClock = field(default_factory=SimulationClock)

    finished: bool = False

    current_stage: int = 1
