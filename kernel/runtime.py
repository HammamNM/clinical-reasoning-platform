from kernel.events import ReasoningEvent
from kernel.registry import EngineRegistry


class KernelRuntime:


    def __init__(self):

        self.registry = EngineRegistry()

        self.event_queue = []



    def register_engine(
        self,
        engine
    ):

        self.registry.register(
            engine
        )



    def publish(
        self,
        event
    ):

        if not isinstance(
            event,
            ReasoningEvent
        ):
            raise TypeError(
                "KernelRuntime accepts only ReasoningEvent"
            )


        self.event_queue.append(
            event
        )



    def run_cycle(
        self,
        session
    ):

        while self.event_queue:

            event = (
                self.event_queue.pop(0)
            )


            new_events = (
                self.registry.dispatch(
                    event,
                    session
                )
            )


            for new_event in new_events:

                self.publish(
                    new_event
                )
