from dataclasses import dataclass


@dataclass
class CognitivePattern:

    name: str

    description: str

    evidence: list


class CognitivePatternExtractor:


    def extract(
        self,
        event_bridge
    ):

        events = event_bridge.get_events()

        patterns = []


        history_requested = False

        investigation_before_history = False


        for event in events:

            if event.event_type == "HISTORY_RESPONSE_REQUEST":

                history_requested = True


            if (

                event.event_type == "INVESTIGATION_RESULT"

                and

                not history_requested

            ):

                investigation_before_history = True


        if investigation_before_history:

            patterns.append(

                CognitivePattern(

                    name="INVESTIGATION_BEFORE_HISTORY",

                    description=(
                        "Student requested investigations before collecting history."
                    ),

                    evidence=[
                        "INVESTIGATION_RESULT"
                    ]

                )

            )


        return patterns
