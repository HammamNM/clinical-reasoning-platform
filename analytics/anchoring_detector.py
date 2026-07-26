class AnchoringDetector:


    def detect(
        self,
        reasoning_state
    ):

        detected = []


        for hypothesis in (
            reasoning_state.active_hypotheses
        ):

            if self.is_anchored(
                hypothesis
            ):

                detected.append({

                    "pattern_id":
                        "CP-201",

                    "hypothesis":
                        hypothesis.name,

                    "reason":
                        "Hypothesis maintained despite contradicting evidence"

                })


        return detected



    def is_anchored(
        self,
        hypothesis
    ):

        has_contradiction = (

            len(
                hypothesis.contradicting_evidence
            ) > 0

        )


        has_high_confidence = (

            hypothesis.confidence >= 0.70

        )


        no_revision = (

            len(
                hypothesis.confidence_history
            ) > 0

            and

            hypothesis.confidence_history[-1].change >= 0

        )


        return (

            has_contradiction

            and

            has_high_confidence

            and

            no_revision

        )
