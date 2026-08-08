from kernel.graph import (
    EdgeRelation
)


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


    def node_by_id(
        self,
        node_id
    ):

        for node in self.graph.nodes:

            if node.id == node_id:

                return node

        return None


    def edges_by_relation(
        self,
        relation
    ):

        if isinstance(
            relation,
            str
        ):

            relation = EdgeRelation(
                relation
            )


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


    def outgoing_by_relation(
        self,
        node_id,
        relation
    ):

        if isinstance(
            relation,
            str
        ):

            relation = EdgeRelation(
                relation
            )


        return [

            edge

            for edge in self.outgoing(
                node_id
            )

            if edge.relation == relation

        ]


    def incoming_by_relation(
        self,
        node_id,
        relation
    ):

        if isinstance(
            relation,
            str
        ):

            relation = EdgeRelation(
                relation
            )


        return [

            edge

            for edge in self.incoming(
                node_id
            )

            if edge.relation == relation

        ]


    def next_nodes(
        self,
        node_id
    ):

        return [

            self.node_by_id(
                edge.target
            )

            for edge in self.outgoing_by_relation(

                node_id,

                EdgeRelation.SEQUENCE

            )

        ]


    def previous_nodes(
        self,
        node_id
    ):

        return [

            self.node_by_id(
                edge.source
            )

            for edge in self.incoming_by_relation(

                node_id,

                EdgeRelation.SEQUENCE

            )

        ]


    def hypotheses_supported_by(
        self,
        minimum_support=1
    ):

        support_counter = {}


        for edge in self.edges_by_relation(
            EdgeRelation.SUPPORTS
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

                >= minimum_support

            ):

                supported.append(
                    node
                )


        return supported


    def hypotheses_with_contradictions(
        self
    ):

        contradiction_targets = set()


        for edge in self.edges_by_relation(
            EdgeRelation.CONTRADICTS
        ):

            contradiction_targets.add(
                edge.target
            )


        return [

            node

            for node in self.graph.nodes

            if node.id in contradiction_targets

        ]


    def confirmed_hypotheses(
        self
    ):

        confirmed_targets = set()


        for edge in self.edges_by_relation(
            EdgeRelation.CONFIRMS
        ):

            confirmed_targets.add(
                edge.target
            )


        return [

            node

            for node in self.graph.nodes

            if node.id in confirmed_targets

        ]


    def rejected_hypotheses(
        self
    ):

        rejected_targets = set()


        for edge in self.edges_by_relation(
            EdgeRelation.REJECTS
        ):

            rejected_targets.add(
                edge.target
            )


        return [

            node

            for node in self.graph.nodes

            if node.id in rejected_targets

        ]


    def evidence_supporting(
        self,
        hypothesis_node_id
    ):

        return [

            self.node_by_id(
                edge.source
            )

            for edge in self.incoming_by_relation(

                hypothesis_node_id,

                EdgeRelation.SUPPORTS

            )

        ]


    def evidence_contradicting(
        self,
        hypothesis_node_id
    ):

        return [

            self.node_by_id(
                edge.source
            )

            for edge in self.incoming_by_relation(

                hypothesis_node_id,

                EdgeRelation.CONTRADICTS

            )

        ]
