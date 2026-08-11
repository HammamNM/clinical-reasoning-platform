from kernel.reasoning_graph_builder import (
    ReasoningGraphBuilder
)

from kernel.events import (
    ReasoningEvent
)

from kernel.registry import (
    EngineRegistry
)

from kernel.session import (
    KernelSession
)

from kernel.reasoning_state_updater import (
    ReasoningStateUpdater
)


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


        self.registry = (
            EngineRegistry()
        )


        self.event_queue = []


        self.graph_builder = (
            ReasoningGraphBuilder()
        )


        self.reasoning_updater = (
            ReasoningStateUpdater()
        )


        self.scenario_engine = None


    def register_engine(
        self,
        engine,
        priority=100
    ):

        self.registry.register(

            engine,

            priority

        )


    def set_scenario_engine(
        self,
        scenario_engine
    ):

        self.scenario_engine = (
            scenario_engine
        )


    def initialize(
        self
    ):

        if self.scenario_engine is None:

            return


        initialization_event = (

            self.scenario_engine.initialize(

                self.session

            )

        )


        if initialization_event is not None:

            self.publish(
                initialization_event
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


            self.graph_builder.process_event(
                event
            )


            generated_events = (

                self.registry.dispatch(

                    event,

                    self.session

                )

            )


            for generated_event in (
                generated_events
            ):

                self.publish(
                    generated_event
                )
