from outcome_engine.rules import OutcomeRuleEngine


class OutcomeEngine:


    def __init__(self):

    self.rule_engine = OutcomeRuleEngine()


    self.rule_engine.add_rule(
        OutcomeRule(
            trigger_event="ECG_COMPLETED",
            status="UNDER_INVESTIGATION",
            severity_change=0,
            description="ECG result available"
        )
    )


    self.rule_engine.add_rule(
        OutcomeRule(
            trigger_event="TROPONIN_COMPLETED",
            status="SUSPECTED_MI",
            severity_change=2,
            description="Positive cardiac biomarker detected"
        )
    )


    self.rule_engine.add_rule(
        OutcomeRule(
            trigger_event="DIAGNOSIS_MADE",
            status="DIAGNOSED",
            severity_change=0,
            description="Diagnosis established"
        )
    )


    def add_rule(
        self,
        rule
    ):

        self.rule_engine.add_rule(
            rule
        )



    def process_event(
        self,
        event,
        outcome
    ):

        self.rule_engine.process_event(
            event,
            outcome
        )


        return outcome
