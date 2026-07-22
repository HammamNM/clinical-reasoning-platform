from decision_engine.base_evaluator import BaseEvaluator
from decision_engine.models import DecisionAssessment


class SafetyEvaluator(BaseEvaluator):


    def evaluate(
        self,
        session,
        action
    ):

        if action in [
            "IGNORE_WARNING",
            "DELAY_EMERGENCY_CARE"
        ]:

            return DecisionAssessment(
                dimension="Safety",
                score=2,
                explanation="Action may compromise patient safety"
            )


        return DecisionAssessment(
            dimension="Safety",
            score=10,
            explanation="No immediate safety concern detected"
        )
