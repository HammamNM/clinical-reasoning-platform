from simulation.state import SimulationState
from simulation.rules import SimulationRule, RuleEngine


state = SimulationState()

engine = RuleEngine()


engine.add_rule(
    SimulationRule(
        trigger_action="ORDER_ECG",
        effect="REVEAL_ECG"
    )
)


print("Before:")
print(state.ecg_visible)


engine.process_action(
    "ORDER_ECG",
    state
)


print("After:")
print(state.ecg_visible)


print("Actions:")
print(state.completed_actions)
