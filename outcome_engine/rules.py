from dataclasses import dataclass


@dataclass
class OutcomeRule:

    trigger_event: str

    outcome_change: str
  
  class OutcomeRuleEngine:


    def __init__(self):

        self.rules = []


    def add_rule(
        self,
        rule
    ):

        self.rules.append(
            rule
        )


    def process_event(
        self,
        event,
        outcome
    ):

        for rule in self.rules:

            if rule.trigger_event == event:

                outcome.description = (
                    rule.outcome_change
                )
