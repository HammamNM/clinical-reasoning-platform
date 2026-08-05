from kernel.models import (
    PrimitiveType
)


class ReasoningAnalyzer:


    def analyze_graph(
        self,
        reasoning_graph
    ):

        node_count = len(
            reasoning_graph.nodes
        )

        edge_count = len(
            reasoning_graph.edges
        )

        primitive_counts = {}


        for node in reasoning_graph.nodes:

            primitive = (
                node.primitive.value
            )

            primitive_counts.setdefault(
                primitive,
                0
            )

            primitive_counts[
                primitive
            ] += 1


        metrics = {

            "nodes":
                node_count,

            "edges":
                edge_count,

            "observations":
                primitive_counts.get(
                    "OBSERVATION",
                    0
                ),

            "investigations":
                primitive_counts.get(
                    "INVESTIGATION",
                    0
                ),

            "hypotheses":
                primitive_counts.get(
                    "HYPOTHESIS",
                    0
                ),

            "decisions":
                primitive_counts.get(
                    "DECISION",
                    0
                ),

            "outcomes":
                primitive_counts.get(
                    "OUTCOME",
                    0
                )

        }


        return metrics



    def extract_reasoning_path(
        self,
        reasoning_graph
    ):

        path = []


        for index, node in enumerate(
            reasoning_graph.nodes,
            start=1
        ):

            path.append({

                "step":
                    index,

                "id":
                    node.id,

                "primitive":
                    node.primitive.value,

                "content":
                    node.content

            })


        return path
