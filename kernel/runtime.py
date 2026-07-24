from kernel.events import ReasoningEvent
from kernel.registry import EngineRegistry
from kernel.session import KernelSession


class KernelRuntime:


    def __init__(
        self,
        session=None
    ):

        self.session = (
            session
            if session
            else KernelSession()
        )

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
        self
    ):

        while self.event_queue:

            event = (
                self.event_queue.pop(0)
            )


            self.session.event_stream.publish(
                event
            )


            generated_events = (
                self.registry.dispatch(
                    event,
                    self.session
                )
            )


            for generated_event in generated_events:

                self.publish(
                    generated_event
                )
