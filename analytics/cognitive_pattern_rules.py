from analytics.evidence import EvidenceExtractor


class CognitivePatternRuleEngine:


    def __init__(self):

        self.evidence_extractor = (
            EvidenceExtractor()
        )


    def evaluate(
        self,
        events
    ):

        detected = []


        evidence = (
            self.investigation_before_history(
                events
            )
        )

        if evidence:

            detected.append({

                "pattern_id": "CP-001",

                "evidence": evidence

            })


        evidence = (
            self.premature_closure(
                events
            )
        )

        if evidence:

            detected.append({

                "pattern_id": "CP-101",

                "evidence": evidence

            })


        return detected


    def investigation_before_history(
        self,
        events
    ):

        history_seen = False

        evidence = []


        for index, event in enumerate(events):

            if event.event_type == (
                "HISTORY_RESPONSE_REQUEST"
            ):

                history_seen = True


            if (

                event.event_type == (
                    "INVESTIGATION_RESULT"
                )

                and

                not history_seen

            ):

                record = (
                    self.evidence_extractor.extract(
                        event,
                        index
                    )
                )


                evidence.append(
                    self.evidence_extractor.to_dict(
                        record
                    )
                )


        return evidence


    def premature_closure(
        self,
        events
    ):

        investigation_seen = False

        evidence = []


        for index, event in enumerate(events):

            if event.event_type == (
                "INVESTIGATION_RESULT"
            ):

                investigation_seen = True


            if event.event_type == (
                "DECISION_ASSESSMENT"
            ):

                if not investigation_seen:

                    record = (
                        self.evidence_extractor.extract(
                            event,
                            index
                        )
                    )


                    evidence.append(
                        self.evidence_extractor.to_dict(
                            record
                        )
                    )


        return evidence
