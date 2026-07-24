from kernel.events import ReasoningEvent


class DecisionEngineAdapter:


    def __init__(
        self,
        decision_engine
    ):

        self.decision_engine = decision_engine



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


        profile = (
            self.decision_engine
            .evaluate_decision(
                session,
                action
            )
        )


        return ReasoningEvent(

            event_type="DECISION_ASSESSMENT",

            payload={
                "action": action,
                "profile": profile
            },

            source="DECISION_ADAPTER"

        )
