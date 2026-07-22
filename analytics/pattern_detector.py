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
