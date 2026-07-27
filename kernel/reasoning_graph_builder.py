from kernel.models import (
    ReasoningUnit,
    PrimitiveType
)

from kernel.graph import ReasoningGraph



class ReasoningGraphBuilder:


    def __init__(
        self
    ):

        self.graph = ReasoningGraph()

        self.counter = 0

        self.last_hypothesis_node = None



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
                event.event_type
            )
        )


        if primitive is None:

            return None


        node = ReasoningUnit(

            id=self.create_node_id(),

            primitive=primitive,

            content=str(
                event.payload
            )

        )


        self.graph.add_node(
            node
        )


        if primitive == PrimitiveType.DECISION:

            self.last_hypothesis_node = node.id



        self.connect_previous(
            node.id
        )



        if (

            primitive == PrimitiveType.INVESTIGATION

            and

            self.last_hypothesis_node is not None

        ):

            self.graph.add_edge(

                node.id,

                self.last_hypothesis_node,

                relation="SUPPORTS"

            )


        return node



    def classify_event(
        self,
        event_type
    ):


        mapping = {


            "HISTORY_RESPONSE_REQUEST":

                PrimitiveType.OBSERVATION,


            "INVESTIGATION_RESULT":

                PrimitiveType.INVESTIGATION,


            "DECISION_ASSESSMENT":

                PrimitiveType.DECISION,


            "OUTCOME_UPDATED":

                PrimitiveType.OUTCOME

        }


        return mapping.get(
            event_type
        )



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

            current_id

        )



    def connect_support(

        self,

        evidence_node_id,

        hypothesis_node_id

    ):

        self.graph.add_edge(

            evidence_node_id,

            hypothesis_node_id,

            relation="SUPPORTS"

        )



    def connect_contradiction(

        self,

        evidence_node_id,

        hypothesis_node_id

    ):

        self.graph.add_edge(

            evidence_node_id,

            hypothesis_node_id,

            relation="CONTRADICTS"

        )
