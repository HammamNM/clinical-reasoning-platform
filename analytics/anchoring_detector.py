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


            evidence = self.get_contradicting_evidence(

                query,

                hypothesis.id

            )


            if len(evidence) == 0:

                continue


            detected.append({

                "pattern_id":
                    "CP-201",

                "name":
                    "Anchoring Bias",

                "hypothesis":
                    hypothesis.content,

                "reason":
                    "Hypothesis remained active despite contradictory evidence",

                "severity":
                    self.calculate_severity(
                        evidence
                    ),

                "evidence":
                    evidence

            })


        return detected



    def get_contradicting_evidence(
        self,
        query,
        hypothesis_id
    ):

        evidence = []


        contradictions = query.edges_by_relation(
            "CONTRADICTS"
        )


        for edge in contradictions:


            if edge.target != hypothesis_id:

                continue


            evidence.append({

                "relation":
                    edge.relation,

                "source":
                    edge.source,

                "target":
                    edge.target

            })


        return evidence



    def calculate_severity(
        self,
        evidence
    ):

        count = len(
            evidence
        )


        if count >= 3:

            return "HIGH"


        if count >= 2:

            return "MEDIUM"


        return "LOW"
