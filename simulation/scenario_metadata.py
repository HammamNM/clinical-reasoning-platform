from dataclasses import dataclass, field



@dataclass
class ScenarioMetadata:


    scenario_id: str

    title: str

    difficulty: str = "BEGINNER"

    learning_objectives: list = field(
        default_factory=list
    )

    target_skills: list = field(
        default_factory=list
    )

    tags: list = field(
        default_factory=list
    )
