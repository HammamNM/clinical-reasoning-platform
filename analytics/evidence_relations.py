from dataclasses import dataclass, asdict


@dataclass
class EvidenceRelation:

    relation_type: str

    before_event_id: str

    after_event_id: str

    before_sequence: int

    after_sequence: int

    before_action: str | None

    after_action: str | None


class EvidenceRelationExtractor:


    def before(
        self,
        before_event,
        before_index,
        after_event,
        after_index
    ):

        return EvidenceRelation(

            relation_type="BEFORE",

            before_event_id=str(
                getattr(
                    before_event,
                    "event_id",
                    ""
                )
            ),

            after_event_id=str(
                getattr(
                    after_event,
                    "event_id",
                    ""
                )
            ),

            before_sequence=before_index,

            after_sequence=after_index,

            before_action=(
                getattr(
                    before_event,
                    "payload",
                    {}
                ).get("action")
            ),

            after_action=(
                getattr(
                    after_event,
                    "payload",
                    {}
                ).get("action")
            )

        )


    def contradicts(
        self,
        evidence_event,
        evidence_index,
        decision_event,
        decision_index
    ):

        return EvidenceRelation(

            relation_type="CONTRADICTS",

            before_event_id=str(
                getattr(
                    evidence_event,
                    "event_id",
                    ""
                )
            ),

            after_event_id=str(
                getattr(
                    decision_event,
                    "event_id",
                    ""
                )
            ),

            before_sequence=evidence_index,

            after_sequence=decision_index,

            before_action=(
                getattr(
                    evidence_event,
                    "payload",
                    {}
                ).get("action")
            ),

            after_action=(
                getattr(
                    decision_event,
                    "payload",
                    {}
                ).get("action")
            )

        )


    def to_dict(
        self,
        relation
    ):

        return asdict(
            relation
        )
