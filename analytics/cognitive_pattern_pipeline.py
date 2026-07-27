from analytics.anchoring_detector import (
    AnchoringDetector
)

from analytics.cognitive_metrics import (
    CognitiveMetricEngine
)


class CognitivePatternPipeline:


    def __init__(self):

        self.anchoring_detector = (
            AnchoringDetector()
        )

        self.metric_engine = (
            CognitiveMetricEngine()
        )


    def analyze(
        self,
        reasoning_graph
    ):

        patterns = []

        patterns.extend(

            self.anchoring_detector.detect(
                reasoning_graph
            )

        )

        metrics = (

            self.metric_engine.evaluate(
                patterns
            )

        )

        return {

            "patterns": patterns,

            "metrics": metrics

        }
