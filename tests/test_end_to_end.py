from kernel.runtime import KernelRuntime
from simulation.orchestrator import SimulationOrchestrator
from analytics.analytics_engine import AnalyticsEngine


def main():

    runtime = KernelRuntime()

    orchestrator = SimulationOrchestrator(
        runtime
    )

    actions = [

        "ASK_CHEST_PAIN",

        "ORDER_ECG",

        "ORDER_TROPONIN",

        "DIAGNOSIS_NSTEMI",

        "TREAT_ASPIRIN"

    ]

    session = orchestrator.run_session(
        actions
    )

    analytics = AnalyticsEngine()

    report = analytics.generate_report(

        session=session,

        reasoning_graph=runtime.graph_builder.graph

    )

    print("\n========== FINAL REPORT ==========\n")

    print(report)


if __name__ == "__main__":

    main()
