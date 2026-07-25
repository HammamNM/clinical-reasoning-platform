class ReportGenerator:


    def generate(
        self,
        session,
        performance_data,
        patterns
    ):

        return {

            "session_id":
                session.session_id,

            "scenario_id":
                session.scenario_id,


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


            "progress_trend":
                performance_data.get(
                    "trend",
                    "INSUFFICIENT_DATA"
                ),


            "patterns":
                patterns,


            "outcome": {

                "status":
                    session.outcome.status,

                "severity":
                    session.outcome.severity,

                "description":
                    session.outcome.description

            }

        }
