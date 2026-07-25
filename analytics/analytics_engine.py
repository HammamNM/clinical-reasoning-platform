from analytics.pattern_detector import PatternDetector
from analytics.performance_analyzer import PerformanceAnalyzer
from analytics.reasoning_analyzer import ReasoningAnalyzer
from analytics.report import ReportGenerator
from analytics.cognitive_patterns import (
    CognitivePatternExtractor
)

from analytics.cognitive_metrics import (
    CognitiveMetricEngine
)



class AnalyticsEngine:


    def __init__(self):

        self.pattern_extractor = (
            CognitivePatternExtractor()
        )

        self.metric_engine = (
            CognitiveMetricEngine()
        )
        
        self.pattern_detector = PatternDetector()

        self.performance_analyzer = (
            PerformanceAnalyzer()
        )

        self.reasoning_analyzer = (
            ReasoningAnalyzer()
        )

        self.report_generator = (
            ReportGenerator()
        )


    def generate_report(
        self,
        session,
        event_bridge,
        reasoning_graph=None
    ):

        patterns = (
            self.pattern_detector.analyze(
                event_bridge
            )
        )

        cognitive_patterns = (
        self.pattern_extractor.extract(
            event_bridge
        )
    )

        cognitive_metrics = (
        self.metric_engine.evaluate(
        cognitive_patterns
        )
    )
        performance_data = (
            self.performance_analyzer.analyze(
                session
            )
        )


        reasoning_data = {}

        reasoning_path = []


        if reasoning_graph is not None:

            reasoning_data = (
                self.reasoning_analyzer.analyze_graph(
                    reasoning_graph
                )
            )

            reasoning_path = (
                self.reasoning_analyzer.extract_reasoning_path(
                    reasoning_graph
                )
            )


        report = (
            self.report_generator.generate(
                session,
                performance_data,
                patterns
            )
        )


        report["reasoning"] = {

            "metrics":
                reasoning_data,

            "path":
                reasoning_path

        }


        return report
