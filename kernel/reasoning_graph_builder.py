from kernel.models import (
    ReasoningUnit,
    PrimitiveType
)

from kernel.graph import (
    ReasoningGraph,
    EdgeRelation
)

from kernel.provenance import (
    ProvenanceRecord
)


class ReasoningGraphBuilder:


    def __init__(
        self
    ):

        self.graph = ReasoningGraph()

        self.counter = 0

        self.last_hypothesis_node = None

        self.last_investigation_node = None

        self.hypothesis_nodes = {}


    def create_node_id(
        self
    ):

        self.counter += 1

        return str(
            self.counter
        )


    def process_event(
        self,
        event
    ):

        primitive = (
            self.classify_event(
                event
            )
        )


        if primitive is None:

            return None


        node = ReasoningUnit(

            id=self.create_node_id(),

            primitive=primitive,

            content=str(
                event.payload
            ),

            provenance=ProvenanceRecord(

                source=event.source,

                event_type=event.event_type

            )

        )


        self.graph.add_node(
            node
        )


        if primitive == PrimitiveType.HYPOTHESIS:

            self.last_hypothesis_node = node.id


            hypothesis_name = (
                event.payload.get(
                    "action"
                )
            )


            if hypothesis_name:

                self.hypothesis_nodes[
                    hypothesis_name
                ] = node.id


        if primitive == PrimitiveType.INVESTIGATION:

            self.last_investigation_node = node.id


        self.connect_previous(
            node.id
        )


        if primitive == PrimitiveType.HYPOTHESIS_UPDATE:

            action = event.payload.get(
                "action",
                ""
            )


            hypothesis_name = (
                action.replace(
                    "CONFIRM_",
                    "DIAGNOSIS_"
                ).replace(
                    "REJECT_",
                    "DIAGNOSIS_"
                )
            )


            hypothesis_node = (
                self.find_hypothesis_node(
                    hypothesis_name
                )
            )


            if hypothesis_node is not None:

                if action.startswith(
                    "CONFIRM_"
                ):

                    self.connect_confirmation(

                        node.id,

                        hypothesis_node.id

                    )


                elif action.startswith(
                    "REJECT_"
                ):

                    self.connect_rejection(

                        node.id,

                        hypothesis_node.id

                    )


        return node


    def classify_event(
        self,
        event
    ):

        payload = getattr(
            event,
            "payload",
            {}
        )


        action = payload.get(
            "action",
            ""
        )


        event_type = event.event_type


        if event_type == "OUTCOME_UPDATED":

            return PrimitiveType.OUTCOME


        if event_type == "INVESTIGATION_RESULT":

            return PrimitiveType.INVESTIGATION


        if event_type == "DECISION_ASSESSMENT":

            return PrimitiveType.DECISION


        if event_type == "ACTION":

            if action.startswith(
                "ASK_"
            ):

                return PrimitiveType.OBSERVATION


            if action.startswith(
                "ORDER_"
            ):

                return PrimitiveType.INVESTIGATION


            if action.startswith(
                "DIAGNOSIS_"
            ):

                return PrimitiveType.HYPOTHESIS


            if action.startswith(
                "CONFIRM_"
            ):

                return PrimitiveType.HYPOTHESIS_UPDATE


            if action.startswith(
                "REJECT_"
            ):

                return PrimitiveType.HYPOTHESIS_UPDATE


            if action.startswith(
                "TREAT_"
            ):

                return PrimitiveType.DECISION


        return None


    def connect_previous(
        self,
        current_id
    ):

        nodes = self.graph.nodes


        if len(nodes) < 2:

            return


        previous = nodes[-2]


        self.graph.add_edge(

            previous.id,

            current_id,

            EdgeRelation.SEQUENCE

        )


    def find_hypothesis_node(
        self,
        hypothesis_name
    ):

        node_id = (
            self.hypothesis_nodes.get(
                hypothesis_name
            )
        )


        if node_id is None:

            return None


        for node in self.graph.nodes:

            if node.id == node_id:

                return node


        return None


    def connect_support(
        self,
        evidence_node_id,
        hypothesis_node_id
    ):

        self.graph.add_edge(

            evidence_node_id,

            hypothesis_node_id,

            EdgeRelation.SUPPORTS

        )


    def connect_contradiction(
        self,
        evidence_node_id,
        hypothesis_node_id
    ):

        self.graph.add_edge(

            evidence_node_id,

            hypothesis_node_id,

            EdgeRelation.CONTRADICTS

        )


    def connect_confirmation(
        self,
        action_node_id,
        hypothesis_node_id
    ):

        self.graph.add_edge(

            action_node_id,

            hypothesis_node_id,

            EdgeRelation.CONFIRMS

        )


    def connect_rejection(
        self,
        action_node_id,
        hypothesis_node_id
    ):

        self.graph.add_edge(

            action_node_id,

            hypothesis_node_id,

            EdgeRelation.REJECTS

        )
