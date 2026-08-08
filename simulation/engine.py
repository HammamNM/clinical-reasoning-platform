from simulation.orchestrator import (
    SimulationOrchestrator
)



class SimulationEngine:


    def __init__(
        self,
        runtime
    ):

        self.runtime = runtime

        self.orchestrator = (

            SimulationOrchestrator(
                runtime
            )

        )



    def execute_action(
        self,
        action
    ):

        self.orchestrator.process_student_action(
            action
        )



    def run(
        self,
        actions
    ):

        return self.orchestrator.run_session(
            actions
        )
