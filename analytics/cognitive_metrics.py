from dataclasses import dataclass


@dataclass
class CognitiveMetric:

    name: str

    score: float

    explanation: str


class CognitiveMetricEngine:



    def evaluate(
        self,
        patterns
    ):

        metrics = []

        total_penalty = len(patterns) * 10

        score = max(
            0.0,
            100.0 - total_penalty
        )

        metrics.append(

            CognitiveMetric(

                name="Clinical Reasoning",

                score=score,

                explanation=self.build_explanation(

                    "Clinical Reasoning",

                    score,

                    patterns

                )

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
