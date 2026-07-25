class ReportGenerator:


    def generate(
        self,
        session,
        performance_data,
        patterns,
        cognitive_data=None
    ):

        cognitive_data = (
            cognitive_data
            if cognitive_data is not None
            else {
                "patterns": [],
                "metrics": []
            }
        )


        cognitive_patterns = []

        for pattern in cognitive_data.get(
            "patterns",
            []
        ):

            cognitive_patterns.append({

                "pattern_id":
                    pattern.pattern_id,

                "name":
                    pattern.name,

                "category":
                    pattern.category,

                "description":
                    pattern.description,

                "evidence":
                    pattern.evidence

            })


        cognitive_metrics = []

        for metric in cognitive_data.get(
            "metrics",
            []
        ):

            cognitive_metrics.append({

                "name":
                    metric.name,

                "score":
                    metric.score,

                "explanation":
                    metric.explanation

            })


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


            "cognitive": {

                "patterns":
                    cognitive_patterns,

                "metrics":
                    cognitive_metrics

            },


            "outcome": {

                "status":
                    session.outcome.status,

                "severity":
                    session.outcome.severity,

                "description":
                    session.outcome.description

            }

        }
