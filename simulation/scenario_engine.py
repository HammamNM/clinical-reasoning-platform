from kernel.events import ReasoningEvent



class ScenarioEngine:


    def __init__(
        self,
        scenario
    ):

        self.scenario = scenario

        self.current_state = (
            scenario.get(
                "current_state",
                "INITIAL"
            )
        )



    def process_action(
        self,
        action,
        session
    ):

        transitions = (
            self.scenario.get(
                "transitions",
                []
            )
        )


        for transition in transitions:

            if transition.get("trigger") == action:


                self.current_state = (
                    transition.get(
                        "next_state"
                    )
                )


                session.event_stream.publish(

                    ReasoningEvent(

                        event_type="STATE_CHANGED",

                        payload={

                            "from":

                                self.current_state,

                            "trigger":

                                action

                        },

                        source="SCENARIO_ENGINE"

                    )

                )


                return self.current_state



        return None
