from dataclasses import dataclass


@dataclass
class GraphEdge:

    source: str

    target: str

    relation: str = "SEQUENCE"

    metadata: dict | None = None



class ReasoningGraph:


    def __init__(self):

        self.nodes = []

        self.edges = []



    def add_node(

        self,

        node

    ):

        self.nodes.append(
            node
        )



    def add_edge(

        self,

        source,

        target,

        relation="SEQUENCE",

        metadata=None

    ):

        self.edges.append(

            GraphEdge(

                source=source,

                target=target,

                relation=relation,

                metadata=metadata

            )

        )



    def find_node(

        self,

        node_id

    ):

        for node in self.nodes:

            if node.id == node_id:

                return node

        return None



    def outgoing_edges(

        self,

        node_id

    ):

        return [

            edge

            for edge in self.edges

            if edge.source == node_id

        ]



    def incoming_edges(

        self,

        node_id

    ):

        return [

            edge

            for edge in self.edges

            if edge.target == node_id

        ]
