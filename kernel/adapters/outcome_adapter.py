from kernel.events import ReasoningEvent


class OutcomeEngineAdapter:


    def __init__(
        self,
        outcome_engine,
        outcome_mapper
    ):

        self.outcome_engine = outcome_engine

        self.outcome_mapper = outcome_mapper



    def process_event(
        self,
        event,
        session
    ):

        if event.event_type != "ACTION":

            return None


        action = (
            event.payload.get(
                "action"
            )
        )


        outcome_event = (
            self.outcome_mapper
            .map_action(
                action
            )
        )


        if not outcome_event:

            return None


        self.outcome_engine.process_event(
            outcome_event,
            session.outcome
        )


        return ReasoningEvent(

            event_type="OUTCOME_UPDATED",

            payload={

                "action": action,

                "outcome": session.outcome

            },

            source="OUTCOME_ADAPTER"

        )
