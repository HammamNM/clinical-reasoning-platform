from simulation.orchestrator import SimulationOrchestrator
from analytics.analytics_engine import AnalyticsEngine


def main():

    orchestrator = SimulationOrchestrator()

    actions = [

        "ASK_CHEST_PAIN",

        "ORDER_ECG",

        "ORDER_TROPONIN",

        "DIAGNOSIS_NSTEMI",

        "TREAT_ASPIRIN"

    ]


    orchestrator.run_session(
        actions
    )


    analytics = AnalyticsEngine()

    report = analytics.generate_report(

        session=orchestrator.kernel_runtime.session,

        reasoning_graph=orchestrator.kernel_runtime.graph_builder.graph

    )


    print("\n========== FINAL REPORT ==========\n")

    print(report)


if __name__ == "__main__":

    main()
