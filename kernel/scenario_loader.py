import json

from kernel.scenario import (
    Scenario
)


class ScenarioLoader:


    def from_dict(
        self,
        data
    ):

        if not isinstance(
            data,
            dict
        ):

            raise TypeError(
                "Scenario data must be a dictionary"
            )


        scenario_id = data.get(
            "scenario_id"
        )


        if not scenario_id:

            raise ValueError(
                "Scenario requires scenario_id"
            )


        title = data.get(
            "title",
            scenario_id
        )


        return Scenario(

            scenario_id=scenario_id,

            title=title,

            specialty=data.get(
                "specialty",
                ""
            ),

            difficulty=data.get(
                "difficulty",
                "medium"
            ),

            patient=data.get(
                "patient",
                {}
            ),

            initial_state=data.get(
                "initial_state",
                {}
            ),

            available_actions=data.get(
                "available_actions",
                []
            ),

            investigations=data.get(
                "investigations",
                {}
            ),

            outcomes=data.get(
                "outcomes",
                {}
            ),

            metadata=data.get(
                "metadata",
                {}
            )

        )


    def from_json(
        self,
        path
    ):

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(
                file
            )


        return self.from_dict(
            data
        )
