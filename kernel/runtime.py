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

from kernel.graph import (
    EdgeRelation
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

        self.registry = EngineRegistry()

        self.event_queue = []

        self.graph_builder = (
            ReasoningGraphBuilder()
        )

        self.reasoning_updater = (
            ReasoningStateUpdater()
        )


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

            event = self.event_queue.pop(0)


            self.session.event_stream.publish(
                event
            )


            self.reasoning_updater.update(

                self.session.reasoning_state,

                event

            )


            node = (
                self.graph_builder.process_event(
                    event
                )
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


            self.connect_evidence_relations(
                event,
                node
            )


    def connect_evidence_relations(
        self,
        event,
        node
    ):

        if event.event_type != (
            "INVESTIGATION_RESULT"
        ):

            return


        if node is None:

            return


        payload = getattr(
            event,
            "payload",
            {}
        )


        supports = payload.get(
            "supports",
            []
        )


        contradicts = payload.get(
            "contradicts",
            []
        )


        for hypothesis_name in supports:

            hypothesis_node = (
                self.find_hypothesis_node(
                    hypothesis_name
                )
            )


            if hypothesis_node is not None:

                self.graph_builder.connect_support(

                    node.id,

                    hypothesis_node.id

                )


        for hypothesis_name in contradicts:

            hypothesis_node = (
                self.find_hypothesis_node(
                    hypothesis_name
                )
            )


            if hypothesis_node is not None:

                self.graph_builder.connect_contradiction(

                    node.id,

                    hypothesis_node.id

                )


    def find_hypothesis_node(
        self,
        hypothesis_name
    ):

        return self.graph_builder.find_hypothesis_node(
            hypothesis_name
        )
        
        
    

        for node in self.graph_builder.graph.nodes:

            if node.primitive.value != "HYPOTHESIS":

                continue


            payload = node.content


            if hypothesis_name in payload:

                return node


        return None
