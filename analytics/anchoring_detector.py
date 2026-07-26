from kernel.query_engine import (
    QueryEngine
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


        candidates = (
            query.hypotheses_with_contradictions()
        )


        for hypothesis in candidates:

            if self.is_anchored(
                hypothesis
            ):

                detected.append({

                    "pattern_id": "CP-201",

                    "hypothesis": hypothesis.content,

                    "reason":
                        "Hypothesis maintained despite contradicting evidence"

                })


        return detected



    def is_anchored(
        self,
        hypothesis
    ):

        if not hasattr(
            hypothesis,
            "confidence"
        ):

            return False


        if hypothesis.confidence < 0.70:

            return False


        history = getattr(
            hypothesis,
            "confidence_history",
            []
        )


        if len(history) == 0:

            return False


        last_change = history[-1].change


        return last_change >= 0
