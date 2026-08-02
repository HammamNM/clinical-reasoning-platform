from kernel.query_engine import QueryEngine
from kernel.models import PrimitiveType



class SearchSatisfactionDetector:


    def detect(
        self,
        reasoning_graph
    ):

        query = QueryEngine(
            reasoning_graph
        )


        detected = []


        investigations = query.nodes_by_primitive(
            PrimitiveType.INVESTIGATION
        )


        decisions = query.nodes_by_primitive(
            PrimitiveType.DECISION
        )


        hypotheses = query.nodes_by_primitive(
            PrimitiveType.HYPOTHESIS
        )


        if len(investigations) != 1:

            return detected



        for hypothesis in hypotheses:


            if not self.has_following_decision(
                query,
                hypothesis.id,
                decisions
            ):

                continue


            detected.append({

                "pattern_id":
                    "CP-205",


                "name":
                    "Search Satisfaction",


                "hypothesis":
                    hypothesis.content,


                "reason":
                    "Reasoning stopped after initial evidence without further investigation"

            })


        return detected



    def has_following_decision(
        self,
        query,
        hypothesis_id,
        decisions
    ):


        for edge in query.outgoing(
            hypothesis_id
        ):

            for decision in decisions:

                if edge.target == decision.id:

                    return True


        return False
