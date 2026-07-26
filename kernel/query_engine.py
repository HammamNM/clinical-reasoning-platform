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


    def hypotheses_supported_by(

    self,

    minimum_support=1

):

    support_counter = {}


    for edge in self.edges_by_relation(
        "SUPPORTS"
    ):

        support_counter.setdefault(
            edge.target,
            0
        )

        support_counter[
            edge.target
        ] += 1


    supported = []


    for node in self.graph.nodes:

        if (

            support_counter.get(
                node.id,
                0
            )

            >=

            minimum_support

        ):

            supported.append(
                node
            )


    def hypotheses_with_contradictions(

    self

):

    contradiction_targets = set()


    for edge in self.edges_by_relation(
        "CONTRADICTS"
    ):

        contradiction_targets.add(
            edge.target
        )


    return [

        node

        for node in self.graph.nodes

        if node.id in contradiction_targets

    ]

    return supported
