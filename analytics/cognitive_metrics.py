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

        penalty = self.calculate_penalty(
            patterns
        )

        score = max(
            0.0,
            100.0 - penalty
        )

        metrics.append(

            CognitiveMetric(

                name="Reasoning Quality",

                score=score,

                explanation=self.build_explanation(

                    "Reasoning Quality",

                    score,

                    patterns

                )

            )

        )

        return metrics


    def calculate_penalty(
        self,
        patterns
    ):

        penalty = 0

        weights = {

            "Anchoring Bias": 15,

            "Premature Closure": 15,

            "Confirmation Bias": 12,

            "Availability Bias": 10,

            "Overconfidence": 10

        }

        for pattern in patterns:

            if isinstance(pattern, dict):

                name = pattern.get(
                    "name",
                    ""
                )

            else:

                name = getattr(
                    pattern,
                    "name",
                    ""
                )

            penalty += weights.get(
                name,
                0
            )

        return penalty


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
