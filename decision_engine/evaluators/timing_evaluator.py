from decision_engine.base_evaluator import BaseEvaluator
from decision_engine.models import DecisionAssessment


class TimingEvaluator(BaseEvaluator):


    def evaluate(
        self,
        session,
        action
    ):

        current_time = session.clock.get_time()


        if current_time <= 5:

            return DecisionAssessment(
                dimension="Timing",
                score=10,
                explanation="Decision made within appropriate time window"
            )


        elif current_time <= 10:

            return DecisionAssessment(
                dimension="Timing",
                score=7,
                explanation="Decision slightly delayed"
            )


        else:

            return DecisionAssessment(
                dimension="Timing",
                score=3,
                explanation="Decision was significantly delayed"
            )
