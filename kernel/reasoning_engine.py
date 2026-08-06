from kernel.reasoning_state_updater import (
    ReasoningStateUpdater
)


class ReasoningEngine:


    def __init__(self):

        self.updater = (
            ReasoningStateUpdater()
        )


    def process_event(
        self,
        event,
        session
    ):

        self.updater.update(

            session.reasoning_state,

            event

        )

        return None
