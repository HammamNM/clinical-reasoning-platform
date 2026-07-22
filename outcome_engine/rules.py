from dataclasses import dataclass


@dataclass
class OutcomeRule:

    trigger_event: str

    status: str

    severity_change: int

    description: str



class OutcomeRuleEngine:


    def __init__(self):

        self.rules = []


    def add_rule(
        self,
        rule
    ):

        self.rules.append(rule)



    def process_event(
        self,
        event,
        outcome
    ):

        for rule in self.rules:

            if rule.trigger_event == event:

                outcome.status = rule.status

                outcome.severity += (
                    rule.severity_change
                )

                outcome.description = (
                    rule.description
                )
