from backend.session_manager import SessionManager
from simulation.orchestrator import SimulationOrchestrator


def main():

    session_manager = SessionManager()

    session = session_manager.create_session(
        student_id="student_001",
        scenario_id="NSTEMI",
        case_path="scenarios/nstemi_case.json"
    )

    orchestrator = SimulationOrchestrator(
        session
    )

    actions = [

        "ASK_CHEST_PAIN",

        "ORDER_ECG",

        "ORDER_TROPONIN",

        "MAKE_DIAGNOSIS"

    ]

    orchestrator.run_session(
        actions
    )

    print(
        "Simulation Finished"
    )


if __name__ == "__main__":

    main()
