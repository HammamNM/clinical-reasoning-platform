from decision_engine.evaluators.efficiency_evaluator import (
    EfficiencyEvaluator
)

from decision_engine.models import (
    DecisionProfile
)

from decision_engine.evaluator_manager import (
    EvaluatorManager
)

from decision_engine.evaluators.timing_evaluator import (
    TimingEvaluator
)

from decision_engine.evaluators.safety_evaluator import (
    SafetyEvaluator
)



class DecisionEngine:


    def __init__(self):

        self.evaluator_manager = (
            EvaluatorManager()
        )


        self.register_evaluator(
            TimingEvaluator()
        )


        self.register_evaluator(
            SafetyEvaluator()
        )


        self.register_evaluator(
            EfficiencyEvaluator()
        )



        self.weights = {

            "Safety": 0.5,

            "Timing": 0.3,

            "Efficiency": 0.2

        }



    def register_evaluator(
        self,
        evaluator
    ):

        self.evaluator_manager.register(
            evaluator
        )



    def calculate_weighted_score(
        self,
        assessments
    ):

        total = 0

        weight_sum = 0


        for assessment in assessments:

            weight = self.weights.get(

                assessment.dimension,

                0

            )


            total += (
                assessment.score
                *
                weight
            )


            weight_sum += weight



        if weight_sum == 0:

            return 0



        return (
            total
            /
            weight_sum
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


        total_score = (

            self.calculate_weighted_score(

                assessments

            )

        )


        return DecisionProfile(

            action=action,

            assessments=assessments,

            total_score=total_score

        )
