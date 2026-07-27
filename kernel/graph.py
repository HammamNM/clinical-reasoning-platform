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

        relation="SEQUENCE"

    ):

        self.edges.append({

            "source": source,

            "target": target,

            "relation": relation

        })



    def outgoing_edges(

        self,

        node_id

    ):

        return [

            edge

            for edge in self.edges

            if edge["source"] == node_id

        ]



    def incoming_edges(

        self,

        node_id

    ):

        return [

            edge

            for edge in self.edges

            if edge["target"] == node_id

        ]
