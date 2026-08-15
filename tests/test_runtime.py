from kernel.runtime import KernelRuntime
from kernel.events import ReasoningEvent


def test_runtime_publishes_event():

    runtime = KernelRuntime()

    event = ReasoningEvent(
        event_type="TEST_EVENT",
        payload={
            "value": 1
        },
        source="TEST"
    )

    runtime.publish(event)

    runtime.run_cycle()

    events = runtime.session.event_stream.get_all()

    assert len(events) == 1

    assert events[0].event_type == "TEST_EVENT"

    assert events[0].payload["value"] == 1


def test_runtime_rejects_invalid_event():

    runtime = KernelRuntime()

    try:

        runtime.publish(
            "INVALID_EVENT"
        )

        assert False

    except TypeError:

        assert True


def test_runtime_initialize_without_scenario():

    runtime = KernelRuntime()

    result = runtime.initialize()

    assert result is runtime

    assert runtime.last_report is None
