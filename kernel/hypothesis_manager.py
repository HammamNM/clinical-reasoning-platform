from kernel.hypothesis import Hypothesis

from kernel.confidence import (
    ConfidenceTracker
)


class HypothesisManager:


    def __init__(self):

        self.confidence_tracker = (
            ConfidenceTracker()
        )


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

        for hypothesis in (
            reasoning_state.active_hypotheses
        ):

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


        self.confidence_tracker.update(

            hypothesis,

            0.15,

            "SUPPORTING_EVIDENCE",

            evidence

        )



    def add_contradicting_evidence(
        self,
        hypothesis,
        evidence
    ):

        hypothesis.contradicting_evidence.append(
            evidence
        )


        self.confidence_tracker.update(

            hypothesis,

            -0.20,

            "CONTRADICTING_EVIDENCE",

            evidence

        )



    def confirm(
        self,
        hypothesis
    ):

        self.confidence_tracker.update(

            hypothesis,

            1.0 - hypothesis.confidence,

            "CONFIRMED"

        )


        hypothesis.status = (
            "CONFIRMED"
        )



    def reject(
        self,
        reasoning_state,
        hypothesis
    ):

        hypothesis.status = (
            "REJECTED"
        )


        reasoning_state.rejected_hypotheses.append(
            hypothesis
        )


        reasoning_state.active_hypotheses.remove(
            hypothesis
        )
