from kernel.query_engine import QueryEngine
from kernel.models import PrimitiveType



class ConfirmationBiasDetector:


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


        decisions = query.nodes_by_primitive(
            PrimitiveType.DECISION
        )


        for hypothesis in hypotheses:


            if not self.has_contradicting_evidence(
                query,
                hypothesis.id
            ):

                continue


            if not self.leads_to_decision(
                query,
                hypothesis.id,
                decisions
            ):

                continue


            detected.append({

                "pattern_id":
                    "CP-203",


                "name":
                    "Confirmation Bias",


                "hypothesis":
                    hypothesis.content,


                "reason":
                    "Decision remained linked to a hypothesis despite contradictory evidence"

            })


        return detected



    def has_contradicting_evidence(
        self,
        query,
        hypothesis_id
    ):


        contradictions = query.edges_by_relation(
            "CONTRADICTS"
        )


        for edge in contradictions:

            if edge.target == hypothesis_id:

                return True


        return False



    def leads_to_decision(
        self,
        query,
        hypothesis_id,
        decisions
    ):


        for edge in query.outgoing(
            hypothesis_id
        ):

            for decision in decisions:

                if (

                    edge.target == decision.id

                ):

                    return True


        return False
