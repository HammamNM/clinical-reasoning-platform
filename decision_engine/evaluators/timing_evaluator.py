from decision_engine.base_evaluator import BaseEvaluator
from decision_engine.models import DecisionAssessment



class TimingEvaluator(BaseEvaluator):


    def evaluate(
        self,
        session,
        action
    ):

        current_time = session.clock.get_time()


        urgent_actions = [

            "ASK_CHEST_PAIN",

            "ORDER_ECG",

            "TREAT_ASPIRIN"

        ]


        investigation_actions = [

            "ORDER_TROPONIN",

            "ORDER_ECHO"

        ]



        # القرارات الحرجة تحتاج استجابة مبكرة

        if action in urgent_actions:


            if current_time <= 3:

                return DecisionAssessment(

                    dimension="Timing",

                    score=10,

                    explanation=
                    "Critical action performed immediately"

                )


            elif current_time <= 7:

                return DecisionAssessment(

                    dimension="Timing",

                    score=6,

                    explanation=
                    "Critical action was delayed"

                )


            else:

                return DecisionAssessment(

                    dimension="Timing",

                    score=3,

                    explanation=
                    "Critical action significantly delayed"

                )



        # الفحوص يمكن أن تتحمل تأخيرًا بسيطًا

        if action in investigation_actions:


            if current_time <= 10:

                return DecisionAssessment(

                    dimension="Timing",

                    score=10,

                    explanation=
                    "Investigation requested within acceptable window"

                )


            else:

                return DecisionAssessment(

                    dimension="Timing",

                    score=5,

                    explanation=
                    "Investigation was delayed"

                )



        # القرارات العامة

        if current_time <= 10:

            return DecisionAssessment(

                dimension="Timing",

                score=8,

                explanation=
                "Decision timing was acceptable"

            )


        return DecisionAssessment(

            dimension="Timing",

            score=4,

            explanation=
            "Decision timing was suboptimal"

        )
