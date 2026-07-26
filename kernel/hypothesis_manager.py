from kernel.hypothesis import Hypothesis


class HypothesisManager:


    def create(
        self,
        reasoning_state,
        hypothesis_name,
        trigger=None
    ):

        hypothesis = Hypothesis(

            name=hypothesis_name,

            confidence=0.50,

            created_by=trigger

        )

        reasoning_state.active_hypotheses.append(
            hypothesis
        )

        return hypothesis


    def find(
        self,
        reasoning_state,
        hypothesis_name
    ):

        for hypothesis in reasoning_state.active_hypotheses:

            if hypothesis.name == hypothesis_name:

                return hypothesis

        return None


    def add_supporting_evidence(

        self,

        hypothesis,

        evidence

    ):

        hypothesis.supporting_evidence.append(
            evidence
        )

        hypothesis.confidence = min(

            1.0,

            hypothesis.confidence + 0.15

        )


    def add_contradicting_evidence(

        self,

        hypothesis,

        evidence

    ):

        hypothesis.contradicting_evidence.append(
            evidence
        )

        hypothesis.confidence = max(

            0.0,

            hypothesis.confidence - 0.20

        )


    def confirm(

        self,

        hypothesis

    ):

        hypothesis.status = "CONFIRMED"

        hypothesis.confidence = 1.0


    def reject(

        self,

        reasoning_state,

        hypothesis

    ):

        hypothesis.status = "REJECTED"

        reasoning_state.rejected_hypotheses.append(
            hypothesis
        )

        reasoning_state.active_hypotheses.remove(
            hypothesis
        )
