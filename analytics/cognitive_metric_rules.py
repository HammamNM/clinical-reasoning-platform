class CognitiveMetricRuleEngine:


    def evaluate(
        self,
        patterns
    ):

        adjustments = {

            "INFORMATION_GATHERING": 0,

            "DIAGNOSTIC_FLEXIBILITY": 0,

            "SAFETY": 0

        }


        for pattern in patterns:

            if pattern.pattern_id == "CP-001":

                adjustments[
                    "INFORMATION_GATHERING"
                ] -= 25

                adjustments[
                    "SAFETY"
                ] -= 10


            if pattern.pattern_id == "CP-101":

                adjustments[
                    "DIAGNOSTIC_FLEXIBILITY"
                ] -= 25

                adjustments[
                    "SAFETY"
                ] -= 15


        return adjustments
