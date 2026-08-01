from kernel.query_engine import (
    QueryEngine
)

from kernel.models import (
    PrimitiveType
)



class AnchoringDetector:


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


        for hypothesis in hypotheses:


            if self.has_contradicting_evidence(
                query,
                hypothesis.id
            ):


                detected.append({

                    "pattern_id":
                        "CP-201",


                    "name":
                        "Anchoring Bias",


                    "hypothesis":

                        hypothesis.content,


                    "reason":

                        "Hypothesis remained active despite contradictory evidence"

                })


        return detected



    def has_contradicting_evidence(
        self,
        query,
        hypothesis_id
    ):


        contradictions = (


            query.edges_by_relation(

                "CONTRADICTS"

            )

        )


        for edge in contradictions:


            if edge["target"] == hypothesis_id:

                return True



        return False
