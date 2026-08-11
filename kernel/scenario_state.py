from dataclasses import dataclass, field


@dataclass
class ScenarioState:

    current_stage: str = "INITIAL"

    completed_actions: list = field(
        default_factory=list
    )

    completed_investigations: list = field(
        default_factory=list
    )

    triggered_events: list = field(
        default_factory=list
    )

    variables: dict = field(
        default_factory=dict
    )

    ended: bool = False

    outcome_id: str = ""
