class ReportGenerator:


    def generate(
        self,
        session,
        performance_data,
        patterns
    ):

        report = {

            "session_id": session.session_id,

            "scenario_id": session.scenario_id,

            "average_score":
                performance_data.get(
                    "average_score",
                    0
                ),

            "dimension_scores":
                performance_data.get(
                    "dimensions",
                    {}
                ),

            "patterns":
                patterns,

            "outcome":
                session.outcome

        }


        return report
