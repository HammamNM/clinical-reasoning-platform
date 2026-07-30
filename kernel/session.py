from dataclasses import dataclass, field
import uuid

from kernel.reasoning_state import (
    ReasoningState
)

from kernel.events import (
    EventStream
)


@dataclass
class KernelSession:


    session_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )


    state: dict = field(
        default_factory=dict
    )


    event_stream: EventStream = field(
        default_factory=EventStream
    )


    metadata: dict = field(
        default_factory=dict
    )


    reasoning_state: ReasoningState = field(
        default_factory=ReasoningState
    )



    decision_history: list = field(
        default_factory=list
    )


    outcome = None


    scenario_id: str = ""
