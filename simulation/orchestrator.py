from kernel.events import ReasoningEvent


class SimulationOrchestrator:

    def __init__(
        self,
        runtime
    ):

        self.runtime = runtime


    def process_student_action(
        self,
        action
    ):

        event = ReasoningEvent(

            event_type="ACTION",

            payload={
                "action": action
            },

            source="STUDENT"

        )

        self.runtime.publish(
            event
        )

        self.runtime.run_cycle()


    def run_session(
        self,
        actions
    ):

        for action in actions:

            self.process_student_action(
                action
            )

        return self.runtime.session
