from analytics.event_bridge import EventBridge
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
print("\nEvents:")

for event in engine.events:
    print(event)
print("TOTAL EVENTS:", len(engine.events))
bridge = EventBridge()

bridge.collect(engine.events)


print("BRIDGED EVENTS:")

for event in bridge.get_events():
    print(event.event_type, "-", event.content)
