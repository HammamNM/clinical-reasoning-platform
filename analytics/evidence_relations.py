from dataclasses import dataclass, asdict


@dataclass
class EvidenceRelation:

    relation_type: str

    before_event_id: str

    after_event_id: str

    before_sequence: int

    after_sequence: int


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

            after_sequence=after_index

        )


    def to_dict(
        self,
        relation
    ):

        return asdict(
            relation
        )
