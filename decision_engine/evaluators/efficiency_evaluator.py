from decision_engine.base_evaluator import BaseEvaluator
from decision_engine.models import DecisionAssessment


class EfficiencyEvaluator(BaseEvaluator):


    def evaluate(
        self,
        session,
        action
    ):

        expensive_actions = [
            "ORDER_UNNECESSARY_CT",
            "ORDER_EXCESSIVE_TESTS"
        ]


        if action in expensive_actions:

            return DecisionAssessment(
                dimension="Efficiency",
                score=3,
                explanation="Resource usage may be excessive"
            )


        return DecisionAssessment(
            dimension="Efficiency",
            score=10,
            explanation="Resource utilization appears appropriate"
        )
