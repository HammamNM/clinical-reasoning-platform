from analytics.pattern_detector import PatternDetector
from analytics.performance_analyzer import PerformanceAnalyzer
from analytics.report import ReportGenerator



class AnalyticsEngine:


    def __init__(self):

        self.pattern_detector = PatternDetector()

        self.performance_analyzer = PerformanceAnalyzer()

        self.report_generator = ReportGenerator()



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


        performance_data = (
            self.performance_analyzer.analyze(
                session
            )
        )


        report = (
            self.report_generator.generate(
                session,
                performance_data,
                patterns
            )
        )


        return report
