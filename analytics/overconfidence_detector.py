from kernel.query_engine import QueryEngine
from kernel.models import PrimitiveType


class OverconfidenceDetector:


    def detect(
        self,
        reasoning_graph
    ):

        query = QueryEngine(
            reasoning_graph
        )

        detected = []

        decisions = query.nodes_by_primitive(
            PrimitiveType.DECISION
        )

        hypotheses = query.nodes_by_primitive(
            PrimitiveType.HYPOTHESIS
        )

        investigations = query.nodes_by_primitive(
            PrimitiveType.INVESTIGATION
        )

        if len(decisions) == 0:

            return detected

        if len(hypotheses) == 0:

            return detected

        if len(investigations) > 0:

            return detected

        contradictions = query.edges_by_relation(
            "CONTRADICTS"
        )

        if len(contradictions) > 0:

            return detected

        for decision in decisions:

            detected.append({

                "pattern_id":
                    "CP-206",

                "name":
                    "Overconfidence",

                "decision":
                    decision.content,

                "reason":
                    "Decision made without seeking additional or contradictory evidence"

            })

        return detected
