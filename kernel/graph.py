from dataclasses import dataclass
from enum import Enum


class EdgeRelation(Enum):

    SEQUENCE = "SEQUENCE"

    SUPPORTS = "SUPPORTS"

    CONTRADICTS = "CONTRADICTS"

    DERIVED_FROM = "DERIVED_FROM"

    CONFIRMS = "CONFIRMS"

    REJECTS = "REJECTS"


@dataclass
class Edge:

    source: str

    target: str

    relation: EdgeRelation = EdgeRelation.SEQUENCE


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
        relation=EdgeRelation.SEQUENCE
    ):

        if isinstance(
            relation,
            str
        ):

            try:

                relation = EdgeRelation(
                    relation
                )

            except ValueError:

                raise ValueError(
                    f"Unknown edge relation: {relation}"
                )


        if not isinstance(
            relation,
            EdgeRelation
        ):

            raise TypeError(
                "relation must be EdgeRelation"
            )


        self.edges.append(

            Edge(

                source=source,

                target=target,

                relation=relation

            )

        )


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

            for edge in self.edges

            if edge.relation == relation

        ]
