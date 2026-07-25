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


        before = len(
            session.event_stream.get_all()
        )


        self.investigation_engine.process_event(
            event,
            session
        )


        after = (
            session.event_stream.get_all()[before:]
        )


        if not after:

            return None


        return after
