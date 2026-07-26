from dataclasses import dataclass


@dataclass
class ReasoningTransition:

    from_state: str

    to_state: str

    trigger: str


class TransitionRecorder:


    def __init__(self):

        self.transitions = []


    def record(

        self,

        from_state,

        to_state,

        trigger

    ):

        self.transitions.append(

            ReasoningTransition(

                from_state=from_state,

                to_state=to_state,

                trigger=trigger

            )

        )
