from kernel.graph_storage import (
    GraphStorage
)

from analytics.analytics_engine import (
    AnalyticsEngine
)
from backend.session_manager import SessionManager
from simulation.orchestrator import SimulationOrchestrator

from kernel.runtime import KernelRuntime

from analytics.analytics_engine import AnalyticsEngine


def main():

    session_manager = SessionManager()


    session = session_manager.create_session(
        student_id="student_001",
        scenario_id="NSTEMI",
        case_path="scenarios/nstemi_case.json"
    )


    runtime = KernelRuntime(
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


    graph_storage = GraphStorage()

    graph_storage.save(

        orchestrator.kernel_runtime
        .graph_builder
        .graph,

        "reasoning_graph.json"

    )
    
    
    analytics = AnalyticsEngine()

    report = analytics.analyze(
    session
    )

    print("\nREPORT")
    print(report)

    report = analytics.generate_report(

        session=session,

        event_bridge=(
            runtime.event_bridge
        ),

        reasoning_graph=(
            runtime
            .reasoning_builder
            .graph
        )

    )


    print(
        "\n=============================="
    )

    print(
        "CLINICAL REASONING REPORT"
    )

    print(
        "=============================="
    )


    print(
        "\nSESSION:"
    )

    print(
        report["session_id"]
    )


    print(
        "\nSCENARIO:"
    )

    print(
        report["scenario_id"]
    )


    print(
        "\nPERFORMANCE:"
    )

    print(
        report["average_score"]
    )


    print(
        "\nDIMENSIONS:"
    )

    print(
        report["dimension_scores"]
    )


    print(
        "\nPROGRESS:"
    )

    print(
        report["progress_trend"]
    )


    print(
        "\nPATTERNS:"
    )

    print(
        report["patterns"]
    )


    print(
        "\nREASONING:"
    )

    print(
        report["reasoning"]
    )


    print(
        "\nOUTCOME:"
    )

    print(
        report["outcome"]
    )


if __name__ == "__main__":

    main()
