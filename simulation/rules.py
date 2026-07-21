from dataclasses import dataclass

from kernel.events import create_event


@dataclass
class SimulationRule:

    trigger_action: str
    effect: str


class RuleEngine:

    def __init__(self):
        self.rules = []
        self.events = []


    def add_rule(self, rule):
        self.rules.append(rule)


    def process_action(self, action, state):

        for rule in self.rules:

            if rule.trigger_action == action:

                if rule.effect == "REVEAL_ECG":
                    state.reveal_ecg()

                    event = create_event(
                        "INFORMATION_REVEALED",
                        "ECG result revealed"
                    )

                    self.events.append(event)


                elif rule.effect == "REVEAL_TROPONIN":
                    state.reveal_troponin()

                    event = create_event(
                        "INFORMATION_REVEALED",
                        "Troponin result revealed"
                    )

                    self.events.append(event)


                state.add_action(action)

                action_event = create_event(
                    "STUDENT_ACTION",
                    action
                )

                self.events.append(action_event)
