from dataclasses import dataclass, field


@dataclass
class SimulationState:

    # Time
    elapsed_minutes: int = 0

    # Patient status
    pain_level: int = 8
    blood_pressure: str = "148/92"
    heart_rate: int = 102
    sweating: bool = True

    # Hidden information
    ecg_visible: bool = False
    troponin_visible: bool = False
    diagnosis_revealed: bool = False

    # Student progress
    completed_actions: list = field(default_factory=list)

    def advance_time(self, minutes=1):
        self.elapsed_minutes += minutes

    def reveal_ecg(self):
        self.ecg_visible = True

    def reveal_troponin(self):
        self.troponin_visible = True

    def add_action(self, action):
        self.completed_actions.append(action)
