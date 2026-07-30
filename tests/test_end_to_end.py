from backend.session import ClinicalSession

from kernel.bootstrap import (
    KernelBootstrap
)

from simulation.orchestrator import (
    SimulationOrchestrator
)

from analytics.analytics_engine import (
    AnalyticsEngine
)


def main():


    clinical_session = ClinicalSession(

        student_id="TEST_STUDENT",

        scenario_id="NSTEMI_TEST"

    )


    bootstrap = KernelBootstrap()


    runtime = bootstrap.create_runtime(
        clinical_session
    )


    orchestrator = SimulationOrchestrator(
        runtime
    )


    actions = [

        "ASK_CHEST_PAIN",

        "ORDER_ECG",

        "ORDER_TROPONIN",

        "DECISION_ASSESSMENT",

        "TREAT_ASPIRIN"

    ]


    session = orchestrator.run_session(
        actions
    )


    analytics = AnalyticsEngine()


    report = analytics.generate_report(

        session,

        runtime.event_bridge
        if hasattr(runtime, "event_bridge")
        else None,

        runtime.graph_builder.graph

    )


    print(
        report
    )


if __name__ == "__main__":

    main()
