from kernel.bootstrap import (
    KernelBootstrap
)

from kernel.scenario_loader import (
    ScenarioLoader
)

from kernel.events import (
    ReasoningEvent
)

from backend.session import (
    ClinicalSession
)


def test_nstemi_full_flow():

    loader = ScenarioLoader()

    scenario = loader.from_json(
        "scenarios/nstemi_basic.json"
    )

    session = ClinicalSession()

    runtime = KernelBootstrap().create_runtime(
        session,
        scenario
    )


    runtime.publish(

        ReasoningEvent(

            event_type="ACTION",

            payload={
                "action": "ASK_HISTORY"
            },

            source="STUDENT"

        )

    )


    runtime.run_cycle()


    runtime.publish(

        ReasoningEvent(

            event_type="ACTION",

            payload={
                "action": "ORDER_ECG"
            },

            source="STUDENT"

        )

    )


    runtime.run_cycle()


    runtime.publish(

        ReasoningEvent(

            event_type="ACTION",

            payload={
                "action": "ORDER_TROPONIN"
            },

            source="STUDENT"

        )

    )


    runtime.run_cycle()


    runtime.publish(

        ReasoningEvent(

            event_type="ACTION",

            payload={
                "action": "DIAGNOSIS_NSTEMI"
            },

            source="STUDENT"

        )

    )


    runtime.run_cycle()


    runtime.publish(

        ReasoningEvent(

            event_type="ACTION",

            payload={
                "action": "TREAT_ACS"
            },

            source="STUDENT"

        )

    )


    runtime.run_cycle()


    events = (
        runtime.session.event_stream.get_all()
    )


    types = [

        event.event_type

        for event in events

    ]

    print(types)
    assert (
        "SCENARIO_INITIALIZED"
        in types
    )


    assert (
        "INVESTIGATION_RESULT"
        in types
    )


    assert (
        "OUTCOME_UPDATED"
        in types
    )


    assert (
        runtime.scenario_engine.state.ended
        is True
    )


if __name__ == "__main__":

    test_nstemi_full_flow()


    print(
        "END-TO-END TEST PASSED"
    )
