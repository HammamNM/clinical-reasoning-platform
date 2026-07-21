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

print("TIME:", session.clock.get_time())

print("ECG BEFORE:", session.state.ecg_visible)

orchestrator.process_student_action("ORDER_ECG")

print("ECG AFTER:", session.state.ecg_visible)

print("TIME:", session.clock.get_time())

print("EVENTS:")

for event in session.event_stream.get_all():
    print(event.event_type, event.content)
