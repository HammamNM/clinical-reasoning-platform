from analytics.pattern_detector import PatternDetector
from backend.session_manager import SessionManager
from simulation.orchestrator import SimulationOrchestrator
from kernel.bootstrap import KernelBootstrap


def main():

    session_manager = SessionManager()

    session = session_manager.create_session(
        student_id="student_001",
        scenario_id="NSTEMI",
        case_path="scenarios/nstemi_case.json"
    )

    runtime = KernelBootstrap().create_runtime(
    session
    )


    orchestrator = SimulationOrchestrator(
    runtime
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

    print("Simulation Finished")

    print("\nEVENTS:")

    for event in session.event_stream.events:
        print(event)


    print("\nDECISIONS:")

    for decision in session.decision_history:
        print(decision)


    print("\nOUTCOME:")

    print(session.outcome)
    print("\nPATTERNS:")

    detector = PatternDetector()

    patterns = detector.analyze(
    runtime.event_bridge 
    )

    print(patterns)

if __name__ == "__main__":

    main()
    
