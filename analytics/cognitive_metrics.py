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


        information_score = 100.0


        for pattern in patterns:

            if pattern.name == "INVESTIGATION_BEFORE_HISTORY":

                information_score -= 25


        metrics.append(

            CognitiveMetric(

                name="INFORMATION_GATHERING",

                score=information_score,

                explanation=(

                    "Measures whether the student gathered sufficient information before acting."

                )

            )

        )


        return metrics
