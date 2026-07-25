from dataclasses import dataclass

from analytics.pattern_registry import PatternRegistry
from analytics.cognitive_pattern_rules import (
    CognitivePatternRuleEngine
)


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

        self.rule_engine = (
            CognitivePatternRuleEngine()
        )


    def extract(
        self,
        event_bridge
    ):

        events = (
            event_bridge.get_events()
        )


        detected_ids = (
            self.rule_engine.evaluate(
                events
            )
        )


        patterns = []


        for pattern_id in detected_ids:

            definition = (
                self.registry.get(
                    pattern_id
                )
            )


            if definition is None:

                continue


            patterns.append(

                CognitivePattern(

                    name=definition.name,

                    description=(
                        definition.description
                    ),

                    evidence=[],

                    pattern_id=(
                        definition.pattern_id
                    ),

                    category=(
                        definition.category
                    )

                )

            )


        return patterns
