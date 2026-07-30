from kernel.events import EventStream

from kernel.reasoning_state import (
    ReasoningState
)


class ClinicalSessionAdapter:


    def __init__(
        self,
        clinical_session
    ):

        self.clinical_session = clinical_session

        self.event_stream = EventStream()

        self.reasoning_state = ReasoningState()


    @property
    def active_case(self):
        return self.clinical_session.active_case


    @property
    def outcome(self):
        return self.clinical_session.outcome


    @property
    def decision_history(self):
        return self.clinical_session.decision_history


    @property
    def state(self):
        return self.clinical_session.state


    @property
    def clock(self):
        return self.clinical_session.clock
