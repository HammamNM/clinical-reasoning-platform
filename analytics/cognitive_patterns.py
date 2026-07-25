from dataclasses import dataclass

from analytics.pattern_registry import PatternRegistry


@dataclass
class CognitivePattern:

    name: str

    description: str

    evidence: list

    pattern_id: str

    category: str


class CognitivePatternExtractor:


    def __init__(self):

        self.registry = PatternRegistry()


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

            definition = self.registry.get(
                "CP-001"
            )


            if definition:

                patterns.append(

                    CognitivePattern(

                        name=definition.name,

                        description=definition.description,

                        evidence=[
                            "INVESTIGATION_RESULT"
                        ],

                        pattern_id=definition.pattern_id,

                        category=definition.category

                    )

                )


        return patterns
