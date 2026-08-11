from kernel.events import (
    ReasoningEvent
)


class ScenarioEngineAdapter:


    def __init__(
        self,
        scenario_engine
    ):

        self.scenario_engine = (
            scenario_engine
        )


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


        generated_events = (
            self.scenario_engine.process_action(

                action,

                session

            )
        )


        if generated_events is None:

            return None


        if isinstance(
            generated_events,
            ReasoningEvent
        ):

            return generated_events


        return [

            generated_event

            for generated_event in generated_events

            if isinstance(
                generated_event,
                ReasoningEvent
            )

        ]
