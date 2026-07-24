from kernel.bootstrap import KernelBootstrap
from kernel.events import ReasoningEvent



def test_runtime_flow():


    runtime = (
        KernelBootstrap()
        .create_runtime()
    )


    event = ReasoningEvent(

        event_type="ACTION",

        payload={

            "action": "ORDER_ECG"

        },

        source="STUDENT"

    )


    runtime.publish(
        event
    )


    runtime.run_cycle()


    print("\nEVENT STREAM:")


    for item in (
        runtime.session
        .event_stream
        .get_all()
    ):

        print(item)



test_runtime_flow()
