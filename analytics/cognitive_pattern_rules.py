class CognitivePatternRuleEngine:


    def evaluate(
        self,
        events
    ):

        detected = []


        if self.investigation_before_history(
            events
        ):

            detected.append(
                "CP-001"
            )


        if self.premature_closure(
            events
        ):

            detected.append(
                "CP-101"
            )


        return detected


    def investigation_before_history(
        self,
        events
    ):

        history_seen = False


        for event in events:

            if event.event_type == (
                "HISTORY_RESPONSE_REQUEST"
            ):

                history_seen = True


            if (

                event.event_type == (
                    "INVESTIGATION_RESULT"
                )

                and

                not history_seen

            ):

                return True


        return False


    def premature_closure(
        self,
        events
    ):

        diagnosis_seen = False

        investigation_seen = False


        for event in events:

            if event.event_type == (
                "INVESTIGATION_RESULT"
            ):

                investigation_seen = True


            if event.event_type == (
                "DECISION_ASSESSMENT"
            ):

                diagnosis_seen = True


                if not investigation_seen:

                    return True


        return False
