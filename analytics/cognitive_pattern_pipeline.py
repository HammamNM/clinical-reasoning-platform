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
        session
    ):

        patterns = []


        anchoring_patterns = (
            self.anchoring_detector.detect(
                session.reasoning_state
            )
        )


        patterns.extend(
            anchoring_patterns
        )


        metrics = (
            self.metric_engine.evaluate(
                patterns
            )
        )


        return {

            "patterns":
                patterns,

            "metrics":
                metrics

        }
