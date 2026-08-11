from dataclasses import dataclass, field


@dataclass
class Scenario:

    scenario_id: str

    title: str

    specialty: str = ""

    difficulty: str = "medium"

    patient: dict = field(
        default_factory=dict
    )

    initial_state: dict = field(
        default_factory=dict
    )

    available_actions: list = field(
        default_factory=list
    )

    investigations: dict = field(
        default_factory=dict
    )

    outcomes: dict = field(
        default_factory=dict
    )

    metadata: dict = field(
        default_factory=dict
    )
