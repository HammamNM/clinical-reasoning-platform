from backend.session import ClinicalSession
from simulation.orchestrator import SimulationOrchestrator
from simulation.rules import SimulationRule


session = ClinicalSession(
    student_id="student_001",
    scenario_id="NSTEMI_001"
)


orchestrator = SimulationOrchestrator(session)


orchestrator.rule_engine.add_rule(
    SimulationRule(
        trigger_action="ORDER_ECG",
        effect="REVEAL_ECG"
    )
)


print("Initial time:")
print(session.clock.get_time())


print("\nInitial ECG:")
print(session.state.ecg_visible)


orchestrator.process_student_action(
    "ORDER_ECG"
)


print("\nAfter action ECG:")
print(session.state.ecg_visible)


print("\nCurrent time:")
print(session.clock.get_time())


print("\nEvents:")

for event in session.event_stream.get_all():
    print(
        event.event_type,
        "-",
        event.content
    )
