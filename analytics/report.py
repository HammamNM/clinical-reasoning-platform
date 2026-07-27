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
