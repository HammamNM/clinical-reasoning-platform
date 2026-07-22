from decision_engine.base_evaluator import BaseEvaluator


class TimingEvaluator(BaseEvaluator):


    def evaluate(
        self,
        session,
        action
    ):

        current_time = session.clock.get_time()


        if current_time <= 5:

            return {
                "dimension": "Timing",
                "value": 10
            }


        elif current_time <= 10:

            return {
                "dimension": "Timing",
                "value": 7
            }


        else:

            return {
                "dimension": "Timing",
                "value": 3
            }
