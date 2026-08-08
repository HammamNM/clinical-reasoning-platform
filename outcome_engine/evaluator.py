class OutcomeEvaluator:


    def evaluate(
        self,
        session,
        action
    ):

        score = 0

        reasons = []


        completed_actions = (

            session.state.completed_actions

        )


        if action not in completed_actions:

            completed_actions.append(
                action
            )


        if "ORDER_ECG" in completed_actions:

            score += 20

            reasons.append(
                "ECG obtained early"
            )


        if "ORDER_TROPONIN" in completed_actions:

            score += 20

            reasons.append(
                "Cardiac biomarker evaluated"
            )


        if "GIVE_ASPIRIN" in completed_actions:

            score += 20

            reasons.append(
                "Appropriate early treatment"
            )


        if "GIVE_HEPARIN" in completed_actions:

            score += 15

            reasons.append(
                "Anticoagulation considered"
            )


        return {

            "score": score,

            "reasons": reasons

        }
