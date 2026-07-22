from backend.session import ClinicalSession
from simulation.orchestrator import SimulationOrchestrator


session = ClinicalSession()

orchestrator = SimulationOrchestrator(
    session
)


orchestrator.process_student_action(
    "ORDER_ECG"
)


print("EVENTS:")

for event in session.event_stream.events:

    print(event)
