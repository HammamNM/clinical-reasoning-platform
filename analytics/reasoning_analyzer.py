class ReasoningAnalyzer:


    def analyze_graph(
        self,
        reasoning_graph
    ):

        metrics = {

            "nodes": len(
                reasoning_graph.nodes
            ),

            "edges": len(
                reasoning_graph.edges
            )

        }


        return metrics



    def extract_reasoning_path(
        self,
        reasoning_graph
    ):

        path = []


        for node in reasoning_graph.nodes:

            path.append(
                {
                    "id": node.id,

                    "primitive":
                        node.primitive.value,

                    "content":
                        node.content
                }
            )


        return path
