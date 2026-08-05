class ReportGenerator:


    def generate(
        self,
        session,
        performance_data,
        patterns,
        cognitive_data=None
    ):

        if cognitive_data is None:

            cognitive_data = {

                "patterns": [],

                "metrics": []

            }


        cognitive_patterns = []


        for pattern in cognitive_data.get(
            "patterns",
            []
        ):

            cognitive_patterns.append({

                "pattern_id":
                    pattern.get(
                        "pattern_id",
                        ""
                    ),

                "name":
                    pattern.get(
                        "name",
                        ""
                    ),

                "reason":
                    pattern.get(
                        "reason",
                        ""
                    ),

                "severity":
                    pattern.get(
                        "severity",
                        "LOW"
                    ),

                "evidence":
                    pattern.get(
                        "evidence",
                        []
                    ),

                "details":
                    pattern

            })


        cognitive_data["patterns"] = (
            cognitive_patterns
        )


        return {

            "session_id":

                session.session_id,


            "scenario_id":

                session.scenario_id,


            "performance": {

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

                    )

            },


            "cognitive":

                cognitive_data,


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
