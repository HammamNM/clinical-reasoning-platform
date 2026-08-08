class ScenarioValidator:


    REQUIRED_FIELDS = {

        "scenario_id",

        "title",

        "patient",

        "investigations",

        "available_actions",

        "transitions"

    }



    def validate(
        self,
        scenario
    ):

        errors = []


        for field in self.REQUIRED_FIELDS:

            if field not in scenario:

                errors.append(

                    f"Missing field: {field}"

                )



        if not isinstance(

            scenario.get(
                "investigations",
                {}
            ),

            dict

        ):

            errors.append(

                "Investigations must be a dictionary"

            )



        if not isinstance(

            scenario.get(
                "transitions",
                []
            ),

            list

        ):

            errors.append(

                "Transitions must be a list"

            )



        for transition in scenario.get(
            "transitions",
            []
        ):

            if "trigger" not in transition:

                errors.append(

                    "Transition missing trigger"

                )


            if "next_state" not in transition:

                errors.append(

                    "Transition missing next_state"

                )



        return {

            "valid":

                len(errors) == 0,

            "errors":

                errors

        }
