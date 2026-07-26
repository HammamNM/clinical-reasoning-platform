from dataclasses import dataclass, field


@dataclass
class ReasoningState:

    active_hypotheses: list = field(
        default_factory=list
    )

    rejected_hypotheses: list = field(
        default_factory=list
    )

    confirmed_hypotheses: list = field(
        default_factory=list
    )

    collected_information: list = field(
        default_factory=list
    )

    ordered_investigations: list = field(
        default_factory=list
    )

    performed_treatments: list = field(
        default_factory=list
    )
