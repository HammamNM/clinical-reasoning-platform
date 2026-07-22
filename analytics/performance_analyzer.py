class PerformanceAnalyzer:


    def calculate_average_score(
        self,
        session
    ):

        if not session.decision_history:

            return 0.0


        total = sum(
            profile.total_score
            for profile in session.decision_history
        )


        return (
            total
            /
            len(session.decision_history)
        )
