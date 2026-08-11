from kernel.events import (
    ReasoningEvent
)


class InvestigationEngine:


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


        if not action:

            return None


        scenario = getattr(
            session,
            "scenario",
            None
        )


        if scenario is None:

            return None


        investigations = (
            scenario.investigations
        )


        investigation_id = (
            self.get_investigation_id(
                action,
                scenario
            )
        )


        if investigation_id is None:

            return None


        investigation = investigations.get(
            investigation_id
        )


        if investigation is None:

            return None


        return ReasoningEvent(

            event_type="INVESTIGATION_RESULT",

            payload={

                "action":
                    action,

                "investigation_id":
                    investigation_id,

                "result":
                    investigation

            },

            source="INVESTIGATION_ENGINE"

        )


    def get_investigation_id(
        self,
        action,
        scenario
    ):

        action_config = (
            scenario.metadata
            .get(
                "actions",
                {}
            )
            .get(
                action
            )
        )


        if action_config is None:

            return None


        return action_config.get(
            "investigation_id"
        )
