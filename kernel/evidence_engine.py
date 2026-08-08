from kernel.evidence import Evidence

from kernel.confidence_engine import (
    ConfidenceEngine
)



class EvidenceEngine:


    def __init__(self):

        self.confidence_engine = (
            ConfidenceEngine()
        )



    def process_event(
        self,
        event,
        session
    ):


        if event.event_type != "INVESTIGATION_RESULT":

            return None



        result = event.payload.get(
            "result",
            {}
        )


        evidence = Evidence(

            source=event.source,

            content=str(result),

            strength=0.2

        )


        if not hasattr(
            session,
            "evidence"
        ):

            session.evidence = []



        session.evidence.append(
            evidence
        )



        hypotheses = getattr(
            session.reasoning_state,
            "hypotheses",
            []
        )



        for hypothesis in hypotheses:


            self.confidence_engine.update_from_evidence(

                hypothesis,

                evidence

            )



        return None
