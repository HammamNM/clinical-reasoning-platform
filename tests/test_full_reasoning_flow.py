from simulation.orchestrator import (
    SimulationOrchestrator
)

from kernel.bootstrap import (
    KernelBootstrap
)

from simulation.session import (
    ClinicalSession
)



def test_investigation_flow():


    clinical_session = ClinicalSession(

        scenario_id="NSTEMI_001",

        active_case={

            "investigations": {

                "ORDER_ECG": {

                    "title": "ECG",

                    "result":
                        "ST depression in lateral leads"

                }

            }

        }

    )


    bootstrap = KernelBootstrap()


    runtime = bootstrap.create_runtime(
        clinical_session
    )


    orchestrator = SimulationOrchestrator(
        runtime
    )


    session = orchestrator.run_session(

        [

            "ORDER_ECG"

        ]

    )


    events = (
        session.event_stream.get_all()
    )


    assert len(events) >= 2


    assert events[0].event_type == "ACTION"


    assert events[1].event_type == "INVESTIGATION_RESULT"
