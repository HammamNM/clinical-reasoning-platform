class QueryEngine:


    def __init__(
        self,
        graph
    ):

        self.graph = graph


    def nodes_by_primitive(

        self,

        primitive

    ):

        return [

            node

            for node in self.graph.nodes

            if node.primitive == primitive

        ]


    def edges_by_relation(

        self,

        relation

    ):

        return [

            edge

            for edge in self.graph.edges

            if edge.relation == relation

        ]


    def outgoing(

        self,

        node_id

    ):

        return self.graph.outgoing_edges(
            node_id
        )


    def incoming(

        self,

        node_id

    ):

        return self.graph.incoming_edges(
            node_id
        )
