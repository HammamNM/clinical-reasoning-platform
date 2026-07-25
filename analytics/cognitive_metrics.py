from dataclasses import dataclass

from analytics.cognitive_metric_rules import (
    CognitiveMetricRuleEngine
)


@dataclass
class CognitiveMetric:

    name: str

    score: float

    explanation: str


class CognitiveMetricEngine:


    def __init__(self):

        self.rule_engine = (
            CognitiveMetricRuleEngine()
        )


    def evaluate(
        self,
        patterns
    ):

        adjustments = (
            self.rule_engine.evaluate(
                patterns
            )
        )


        metrics = []


        for name, adjustment in (
            adjustments.items()
        ):

            score = 100.0 + adjustment


            score = max(
                0.0,
                min(
                    100.0,
                    score
                )
            )


            explanation = (
                self.build_explanation(
                    name,
                    score,
                    patterns
                )
            )


            metrics.append(

                CognitiveMetric(

                    name=name,

                    score=score,

                    explanation=explanation

                )

            )


        return metrics


    def build_explanation(
        self,
        name,
        score,
        patterns
    ):

        if score >= 90:

            return (
                f"{name} is strong."
            )


        if score >= 75:

            return (
                f"{name} is acceptable "
                f"but has room for improvement."
            )


        if score >= 50:

            return (
                f"{name} shows a meaningful "
                f"area for improvement."
            )


        return (
            f"{name} shows a significant "
            f"weakness."
        )
