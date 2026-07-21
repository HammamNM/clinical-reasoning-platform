from dataclasses import dataclass


@dataclass
class SimulationRule:

    trigger_action: str
    effect: str


class RuleEngine:

    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def process_action(self, action, state):

        for rule in self.rules:

            if rule.trigger_action == action:

                if rule.effect == "REVEAL_ECG":
                    state.reveal_ecg()

                elif rule.effect == "REVEAL_TROPONIN":
                    state.reveal_troponin()

                state.add_action(action)
