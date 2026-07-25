from analytics.event_bridge import EventBridge
from kernel.events import ReasoningEvent
from kernel.registry import EngineRegistry
from kernel.session import KernelSession
from kernel.reasoning_graph_builder import ReasoningGraphBuilder

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
        self.event_bridge = EventBridge()
        self.reasoning_builder = ReasoningGraphBuilder()

    
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


            self.event_bridge.collect(
                event
            )

            self.reasoning_builder.process_event(
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
