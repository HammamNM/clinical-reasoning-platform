from outcome_engine.rules import OutcomeRuleEngine


class OutcomeEngine:


    def __init__(self):

        self.rule_engine = OutcomeRuleEngine()



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
