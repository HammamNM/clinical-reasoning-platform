from analytics.evidence import EvidenceExtractor

from analytics.evidence_relations import (
    EvidenceRelationExtractor
)


class CognitivePatternRuleEngine:


    def __init__(self):

        self.evidence_extractor = (
            EvidenceExtractor()
        )

        self.relation_extractor = (
            EvidenceRelationExtractor()
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

        first_history_index = None

        first_history_event = None

        evidence = []


        for index, event in enumerate(events):

            if event.event_type == (
                "HISTORY_RESPONSE_REQUEST"
            ):

                first_history_index = index

                first_history_event = event

                break


        if first_history_index is None:

            return []


        for index, event in enumerate(events):

            if (

                event.event_type == (
                    "INVESTIGATION_RESULT"
                )

                and

                index < first_history_index

            ):

                event_record = (
                    self.evidence_extractor.extract(
                        event,
                        index
                    )
                )


                relation = (
                    self.relation_extractor.before(
                        event,
                        index,
                        first_history_event,
                        first_history_index
                    )
                )


                evidence.append({

                    "event":
                        self.evidence_extractor.to_dict(
                            event_record
                        ),

                    "relation":
                        self.relation_extractor.to_dict(
                            relation
                        )

                })


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
