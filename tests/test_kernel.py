from kernel.models import ReasoningUnit, PrimitiveType
from kernel.graph import ReasoningGraph
from kernel.events import ReasoningEvent


def test_reasoning_flow():

    observation = ReasoningUnit(
        id="1",
        primitive=PrimitiveType.OBSERVATION,
        content="Chest pain with sweating"
    )

    hypothesis = ReasoningUnit(
        id="2",
        primitive=PrimitiveType.HYPOTHESIS,
        content="Acute Coronary Syndrome"
    )

    decision = ReasoningUnit(
        id="3",
        primitive=PrimitiveType.DECISION,
        content="Order ECG"
    )


    graph = ReasoningGraph()

    graph.add_node(observation)
    graph.add_node(hypothesis)
    graph.add_node(decision)


    graph.add_edge("1", "2")
    graph.add_edge("2", "3")


    event = ReasoningEvent(
        event_id="E001",
        event_type="DECISION",
        content="Student ordered ECG"
    )


    print("Nodes:")
    for node in graph.nodes:
        print(node)


    print("\nEdges:")
    for edge in graph.edges:
        print(edge)


    print("\nEvent:")
    print(event)


test_reasoning_flow()
