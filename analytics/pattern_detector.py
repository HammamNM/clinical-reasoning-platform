class CognitivePatternDetector:


    def detect_delayed_decisions(
        self,
        session
    ):

        timing_scores = []


        for profile in session.decision_history:

            for assessment in profile.assessments:

                if assessment.dimension == "Timing":

                    timing_scores.append(
                        assessment.score
                    )


        if len(timing_scores) < 3:

            return "INSUFFICIENT_DATA"


        average = (
            sum(timing_scores)
            /
            len(timing_scores)
        )


        if average <= 5:

            return "DELAYED_DECISION_PATTERN"


        return "NO_PATTERN"

    def detect_overtesting_pattern(
        self,
        session
    ):

        efficiency_scores = []


        for profile in session.decision_history:

            for assessment in profile.assessments:

                if assessment.dimension == "Efficiency":

                    efficiency_scores.append(
                        assessment.score
                    )


        if len(efficiency_scores) < 3:

            return "INSUFFICIENT_DATA"


        average = (
            sum(efficiency_scores)
            /
            len(efficiency_scores)
        )


        if average <= 5:

            return "OVERTESTING_PATTERN"


        return "NO_PATTERN"

    def detect_premature_closure(
        self,
        session
    ):

        reasoning_events = (
            session.event_stream.events
        )


        if len(reasoning_events) < 3:

            return "INSUFFICIENT_DATA"


        confirmation_events = 0


        ignored_evidence_events = 0


        for event in reasoning_events:

            if (
                event.get("event_type")
                ==
                "CONFIRMATION_ONLY"
            ):

                confirmation_events += 1


            if (
                event.get("event_type")
                ==
                "IGNORED_EVIDENCE"
            ):

                ignored_evidence_events += 1



        if (
            confirmation_events >= 2
            and
            ignored_evidence_events >= 1
        ):

            return "PREMATURE_CLOSURE_PATTERN"



        return "NO_PATTERN"
