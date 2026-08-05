class InvestigationEngineAdapter:


    def __init__(
        self,
        investigation_engine
    ):

        self.investigation_engine = (
            investigation_engine
        )


    def process_event(
        self,
        event,
        session
    ):

        return self.investigation_engine.process_event(
            event,
            session
        )
