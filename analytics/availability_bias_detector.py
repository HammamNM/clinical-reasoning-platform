from kernel.query_engine import QueryEngine
from kernel.models import PrimitiveType



class AvailabilityBiasDetector:


    def detect(
        self,
        reasoning_graph
    ):

        query = QueryEngine(
            reasoning_graph
        )


        detected = []


        hypotheses = query.nodes_by_primitive(
            PrimitiveType.HYPOTHESIS
        )


        investigations = query.nodes_by_primitive(
            PrimitiveType.INVESTIGATION
        )


        for hypothesis in hypotheses:


            if len(investigations) > 0:

                continue


            if not self.has_observation_support(
                query,
                hypothesis.id
            ):

                continue


            detected.append({

                "pattern_id":
                    "CP-204",


                "name":
                    "Availability Bias",


                "hypothesis":
                    hypothesis.content,


                "reason":
                    "Hypothesis selected with limited evidence and no investigation"

            })


        return detected



    def has_observation_support(
        self,
        query,
        hypothesis_id
    ):


        for edge in query.incoming(
            hypothesis_id
        ):

            if edge.relation == "SUPPORTS":

                return True


        return False
