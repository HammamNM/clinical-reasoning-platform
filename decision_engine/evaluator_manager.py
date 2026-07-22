class EvaluatorManager:


    def __init__(self):

        self.evaluators = []


    def register(
        self,
        evaluator
    ):

        self.evaluators.append(
            evaluator
        )


    def evaluate(
        self,
        session,
        action
    ):

        decision_vector = []


        for evaluator in self.evaluators:

            result = evaluator.evaluate(
                session,
                action
            )

            decision_vector.append(
                result
            )


        return decision_vector
