from decision_engine.base_evaluator import BaseEvaluator
from decision_engine.models import DecisionAssessment



class EfficiencyEvaluator(BaseEvaluator):


    def evaluate(
        self,
        session,
        action
    ):

        unnecessary_actions = [

            "ORDER_UNNECESSARY_CT",

            "ORDER_EXCESSIVE_TESTS",

            "REPEAT_NORMAL_TEST"

        ]


        if action in unnecessary_actions:

            return DecisionAssessment(

                dimension="Efficiency",

                score=3,

                explanation=
                "Resource usage may be unnecessary"

            )



        outcome = session.outcome

        status = getattr(
            outcome,
            "status",
            ""
        )



        # فحوص مناسبة عند الاشتباه القلبي

        cardiac_investigations = [

            "ORDER_ECG",

            "ORDER_TROPONIN",

            "ORDER_ECHO"

        ]


        if (

            status in [

                "SUSPECTED_MI",

                "UNDER_INVESTIGATION"

            ]

            and

            action in cardiac_investigations

        ):

            return DecisionAssessment(

                dimension="Efficiency",

                score=10,

                explanation=
                "Investigation is appropriate for current clinical context"

            )



        # العلاج المناسب لا يعتبر هدرًا

        if action.startswith(
            "TREAT_"
        ):

            return DecisionAssessment(

                dimension="Efficiency",

                score=9,

                explanation=
                "Treatment choice appears resource appropriate"

            )



        # الفحوص غير المرتبطة بالحالة

        if action.startswith(
            "ORDER_"
        ):

            return DecisionAssessment(

                dimension="Efficiency",

                score=7,

                explanation=
                "Investigation may be useful but requires clinical justification"

            )



        return DecisionAssessment(

            dimension="Efficiency",

            score=8,

            explanation=
            "Resource utilization appears acceptable"

        )
