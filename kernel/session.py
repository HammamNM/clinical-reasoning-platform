from dataclasses import dataclass, field
import uuid

from kernel.events import EventStream


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
