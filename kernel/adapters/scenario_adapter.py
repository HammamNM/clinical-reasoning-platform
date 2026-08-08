from kernel.events import ReasoningEvent



class ScenarioEngineAdapter:


    def __init__(
        self,
        scenario_engine
    ):

        self.scenario_engine = scenario_engine



    def process_event(
        self,
        event,
        session
    ):

        if event.event_type != "ACTION":

            return None


        action = event.payload.get(
            "action"
        )


        if action is None:

            return None



        new_state = (

            self.scenario_engine.process_action(

                action,

                session

            )

        )


        if new_state is None:

            return None



        return ReasoningEvent(

            event_type="STATE_CHANGED",

            payload={

                "state":

                    new_state,

                "trigger":

                    action

            },

            source="SCENARIO_ADAPTER"

        )
