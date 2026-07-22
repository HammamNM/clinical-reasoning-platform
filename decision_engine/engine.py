from decision_engine.models import DecisionProfile
from decision_engine.evaluator_manager import EvaluatorManager
from decision_engine.evaluators.timing_evaluator import TimingEvaluator
from decision_engine.evaluators.safety_evaluator import SafetyEvaluator

class DecisionEngine:


   def __init__(self):

    self.evaluator_manager = EvaluatorManager()


    self.register_evaluator(
        TimingEvaluator()
    )


    self.register_evaluator(
        SafetyEvaluator()
    ) 


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
