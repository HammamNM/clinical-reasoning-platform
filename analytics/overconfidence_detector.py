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


        investigations = query.nodes_by_primitive(
            PrimitiveType.INVESTIGATION
        )


        hypotheses = query.nodes_by_primitive(
            PrimitiveType.HYPOTHESIS
        )


        if len(investigations) > 0:

            return detected



        if len(hypotheses) == 0:

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
                    "Decision made with limited supporting evidence"

            })


        return detected
