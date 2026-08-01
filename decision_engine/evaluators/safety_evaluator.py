from decision_engine.base_evaluator import BaseEvaluator
from decision_engine.models import DecisionAssessment



class SafetyEvaluator(BaseEvaluator):


    def evaluate(
        self,
        session,
        action
    ):

        outcome = session.outcome

        severity = getattr(
            outcome,
            "severity",
            0
        )


        critical_actions = [

            "IGNORE_WARNING",

            "DELAY_EMERGENCY_CARE",

            "DISCHARGE_HIGH_RISK_PATIENT"

        ]


        if action in critical_actions:

            return DecisionAssessment(

                dimension="Safety",

                score=2,

                explanation=
                "Action may compromise patient safety"

            )


        if (

            severity >= 2

            and

            action == "WAIT"

        ):

            return DecisionAssessment(

                dimension="Safety",

                score=4,

                explanation=
                "Delay may be unsafe in a high-risk patient"

            )


        if (

            severity >= 2

            and

            action == "TREAT_ASPIRIN"

        ):

            return DecisionAssessment(

                dimension="Safety",

                score=10,

                explanation=
                "Treatment is appropriate for current risk level"

            )


        return DecisionAssessment(

            dimension="Safety",

            score=8,

            explanation=
            "No major safety issue detected"

        )
