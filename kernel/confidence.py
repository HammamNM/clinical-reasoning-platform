from dataclasses import dataclass, field


@dataclass
class ConfidenceChange:

    old_value: float

    new_value: float

    change: float

    reason: str

    evidence: dict = field(
        default_factory=dict
    )


class ConfidenceTracker:


    def update(

        self,

        hypothesis,

        delta,

        reason,

        evidence=None

    ):

        old_value = (
            hypothesis.confidence
        )


        new_value = max(

            0.0,

            min(

                1.0,

                old_value + delta

            )

        )


        hypothesis.confidence = (
            new_value
        )


        if not hasattr(
            hypothesis,
            "confidence_history"
        ):

            hypothesis.confidence_history = []


        hypothesis.confidence_history.append(

            ConfidenceChange(

                old_value=old_value,

                new_value=new_value,

                change=delta,

                reason=reason,

                evidence=evidence or {}

            )

        )


        return new_value
