class ReasoningAnalyzer:


    def extract_reasoning_metrics(
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
