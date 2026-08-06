from enum import Enum


class ReasoningPhase(Enum):

    OBSERVATION = "OBSERVATION"

    HYPOTHESIS = "HYPOTHESIS"

    INVESTIGATION = "INVESTIGATION"

    DECISION = "DECISION"

    OUTCOME = "OUTCOME"


class ReasoningCycle:


    def __init__(self):

        self.phase = (
            ReasoningPhase.OBSERVATION
        )


    def move_to(
        self,
        phase
    ):

        self.phase = phase


    def current_phase(
        self
    ):

        return self.phase
