from kernel.reasoning_graph_builder import ReasoningGraphBuilder
from kernel.events import ReasoningEvent


builder = ReasoningGraphBuilder()


events = [

    ReasoningEvent(
        event_type="HISTORY_RESPONSE_REQUEST",
        payload={"question": "Chest pain"},
        source="TEST"
    ),

    ReasoningEvent(
        event_type="INVESTIGATION_RESULT",
        payload={"test": "ECG"},
        source="TEST"
    ),

    ReasoningEvent(
        event_type="DECISION_ASSESSMENT",
        payload={"decision": "NSTEMI"},
        source="TEST"
    ),

    ReasoningEvent(
        event_type="OUTCOME_UPDATED",
        payload={"status": "DIAGNOSED"},
        source="TEST"
    )

]


for event in events:

    builder.process_event(event)


print("\nNODES")

for node in builder.graph.nodes:

    print(node)


print("\nEDGES")

for edge in builder.graph.edges:

    print(edge)
