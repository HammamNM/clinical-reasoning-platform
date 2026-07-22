from decision_engine.models import DecisionProfile
from decision_engine.evaluator_manager import EvaluatorManager


class DecisionEngine:


    def __init__(self):

        self.evaluator_manager = EvaluatorManager()



    def register_evaluator(
        self,
        evaluator
    ):

        self.evaluator_manager.register(
            evaluator
        )



    def evaluate_decision(
        self,
        session,
        action
    ):

        assessments = (
            self.evaluator_manager.evaluate(
                session,
                action
            )
        )


        return DecisionProfile(
    action=action,
    assessments=assessments
        )
