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


        payload = getattr(
            event,
            "payload",
            {}
        )


        result = payload.get(
            "result",
            ""
        )


        supports = payload.get(
            "supports",
            []
        )


        contradicts = payload.get(
            "contradicts",
            []
        )


        strength = payload.get(
            "strength",
            1.0
        )


        evidence = Evidence(

            source=event.source,

            content=str(
                result
            ),

            supports=list(
                supports
            ),

            contradicts=list(
                contradicts
            ),

            strength=float(
                strength
            )

        )


        if not hasattr(
            session,
            "evidence"
        ):

            session.evidence = []


        session.evidence.append(
            evidence
        )


        for hypothesis_name in supports:

            hypothesis = (
                self.hypothesis_manager.find(
                    session.reasoning_state,
                    hypothesis_name
                )
            )


            if hypothesis is not None:

                self.hypothesis_manager.add_supporting_evidence(

                    hypothesis,

                    evidence

                )


        for hypothesis_name in contradicts:

            hypothesis = (
                self.hypothesis_manager.find(
                    session.reasoning_state,
                    hypothesis_name
                )
            )


            if hypothesis is not None:

                self.hypothesis_manager.add_contradicting_evidence(

                    hypothesis,

                    evidence

                )


        return None
