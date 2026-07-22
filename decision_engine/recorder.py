class DecisionRecorder:


    def __init__(
        self,
        decision_engine
    ):

        self.decision_engine = decision_engine



    def record(
        self,
        session,
        action
    ):

        profile = (
            self.decision_engine
            .evaluate_decision(
                session,
                action
            )
        )


        session.event_stream.add(
            {
                "event_type": "DECISION_ASSESSMENT",
                "content": profile
            }
        )


        return profile
