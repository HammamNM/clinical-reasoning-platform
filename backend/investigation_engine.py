class InvestigationEngine:


    def process_action(
        self,
        action,
        case_data,
        event_stream
    ):

        investigations = case_data.get(
            "investigations",
            {}
        )


        if action in investigations:

            result = investigations[action]


            event_stream.add(
                {
                    "event_type": "INVESTIGATION_RESULT",
                    "content": result
                }
            )
