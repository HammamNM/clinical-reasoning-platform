from simulation.action_processor import (
    ActionProcessor
)


class SimulationOrchestrator:


    def __init__(
        self,
        runtime
    ):

        self.runtime = runtime

        self.action_processor = (
            ActionProcessor()
        )



    def process_student_action(
        self,
        action,
        payload=None
    ):

        event = (
            self.action_processor.process(
                action,
                payload
            )
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
