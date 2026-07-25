from dataclasses import dataclass, asdict


@dataclass
class EvidenceRecord:

    event_id: str

    event_type: str

    sequence_index: int

    action: str | None

    payload: dict

    source: str | None

    timestamp: str | None


class EvidenceExtractor:


    def extract(
        self,
        event,
        sequence_index
    ):

        payload = getattr(
            event,
            "payload",
            {}
        )


        return EvidenceRecord(

            event_id=str(
                getattr(
                    event,
                    "event_id",
                    ""
                )
            ),

            event_type=str(
                getattr(
                    event,
                    "event_type",
                    ""
                )
            ),

            sequence_index=(
                sequence_index
            ),

            action=payload.get(
                "action"
            ),

            payload=payload,

            source=getattr(
                event,
                "source",
                None
            ),

            timestamp=str(
                getattr(
                    event,
                    "timestamp",
                    None
                )
            )

        )


    def to_dict(
        self,
        evidence
    ):

        return asdict(
            evidence
        )
