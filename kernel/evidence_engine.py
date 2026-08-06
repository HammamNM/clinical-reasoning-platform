from kernel.evidence import (
    Evidence
)

from kernel.hypothesis_manager import (
    HypothesisManager
)


class EvidenceEngine:


    def __init__(self):

        self.hypothesis_manager = (
            HypothesisManager()
        )


    def process_event(
        self,
        event,
        session
    ):

        if event.event_type != (
            "INVESTIGATION_RESULT"
        ):

            return None


        evidence = Evidence(

            evidence_id=event.event_id,

            evidence_type=event.event_type,

            source=event.source,

            content=event.payload

        )


        for hypothesis in (

            session.reasoning_state.active_hypotheses

        ):

            self.hypothesis_manager.add_supporting_evidence(

                hypothesis,

                evidence

            )


        return None
