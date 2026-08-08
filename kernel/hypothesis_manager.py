from kernel.hypothesis import (
    Hypothesis
)

from kernel.confidence import (
    ConfidenceTracker
)


class HypothesisManager:


    VALID_STATUSES = {
        "ACTIVE",
        "CONFIRMED",
        "REJECTED"
    }


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

        existing = self.find(
            reasoning_state,
            hypothesis_name
        )


        if existing is not None:

            return existing


        hypothesis = Hypothesis(

            name=hypothesis_name,

            confidence=0.50,

            status="ACTIVE",

            created_by=trigger

        )


        reasoning_state.active_hypotheses.append(
            hypothesis
        )


        if hasattr(
            reasoning_state,
            "hypotheses"
        ):

            reasoning_state.hypotheses.append(
                hypothesis
            )


        return hypothesis


    def find(
        self,
        reasoning_state,
        hypothesis_name
    ):

        for hypothesis in (
            reasoning_state.hypotheses
        ):

            if hypothesis.name == hypothesis_name:

                return hypothesis


        return None


    def add_supporting_evidence(
        self,
        hypothesis,
        evidence
    ):

        if hypothesis.status != "ACTIVE":

            return


        if evidence not in (
            hypothesis.supporting_evidence
        ):

            hypothesis.supporting_evidence.append(
                evidence
            )


        strength = getattr(
            evidence,
            "strength",
            1.0
        )


        self.confidence_tracker.update(

            hypothesis,

            0.15 * strength,

            "SUPPORTING_EVIDENCE",

            evidence

        )


        if hasattr(
            evidence,
            "supports"
        ):

            if hypothesis.name not in evidence.supports:

                evidence.supports.append(
                    hypothesis.name
                )


    def add_contradicting_evidence(
        self,
        hypothesis,
        evidence
    ):

        if hypothesis.status != "ACTIVE":

            return


        if evidence not in (
            hypothesis.contradicting_evidence
        ):

            hypothesis.contradicting_evidence.append(
                evidence
            )


        strength = getattr(
            evidence,
            "strength",
            1.0
        )


        self.confidence_tracker.update(

            hypothesis,

            -0.20 * strength,

            "CONTRADICTING_EVIDENCE",

            evidence

        )


        if hasattr(
            evidence,
            "contradicts"
        ):

            if hypothesis.name not in evidence.contradicts:

                evidence.contradicts.append(
                    hypothesis.name
                )


    def confirm(
        self,
        hypothesis
    ):

        if hypothesis.status != "ACTIVE":

            return False


        self.confidence_tracker.update(

            hypothesis,

            1.0 - hypothesis.confidence,

            "CONFIRMED"

        )


        hypothesis.status = "CONFIRMED"


        return True


    def reject(
        self,
        reasoning_state,
        hypothesis
    ):

        if hypothesis.status != "ACTIVE":

            return False


        hypothesis.status = "REJECTED"


        if hypothesis not in (
            reasoning_state.rejected_hypotheses
        ):

            reasoning_state.rejected_hypotheses.append(
                hypothesis
            )


        if hypothesis in (
            reasoning_state.active_hypotheses
        ):

            reasoning_state.active_hypotheses.remove(
                hypothesis
            )


        return True
