from kernel.events import ReasoningEvent


class InvestigationEngineAdapter:


    def __init__(
        self,
        investigation_engine
    ):

        self.investigation_engine = investigation_engine



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


        before_count = len(
            session.event_stream.get_all()
        )


        self.investigation_engine.process_action(
            action,
            session.active_case,
            session.event_stream
        )


        after_events = (
            session.event_stream.get_all()
            [before_count:]
        )


        if not after_events:

            return None


        old_event = after_events[0]


        return ReasoningEvent(

            event_type="INVESTIGATION_RESULT",

            payload={

                "action": action,

                "result": old_event

            },

            source="INVESTIGATION_ADAPTER"

        )
