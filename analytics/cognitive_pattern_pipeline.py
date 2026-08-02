from analytics.anchoring_detector import (
    AnchoringDetector
)

from analytics.premature_closure_detector import (
    PrematureClosureDetector
)

from analytics.confirmation_bias_detector import (
    ConfirmationBiasDetector
)

from analytics.availability_bias_detector import (
    AvailabilityBiasDetector
)

from analytics.search_satisfaction_detector import (
    SearchSatisfactionDetector
)

from analytics.cognitive_metrics import (
    CognitiveMetricEngine
)



class CognitivePatternPipeline:


    def __init__(self):

        self.detectors = [

            AnchoringDetector(),

            PrematureClosureDetector(),

            ConfirmationBiasDetector(),

            AvailabilityBiasDetector(),

            SearchSatisfactionDetector()

        ]


        self.metric_engine = (
            CognitiveMetricEngine()
        )



    def analyze(
        self,
        reasoning_graph
    ):


        patterns = []


        for detector in self.detectors:


            detected_patterns = detector.detect(

                reasoning_graph

            )


            patterns.extend(

                detected_patterns

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
