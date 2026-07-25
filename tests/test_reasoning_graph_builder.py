from kernel.reasoning_graph_builder import ReasoningGraphBuilder
from kernel.events import ReasoningEvent


def test_reasoning_graph_builder():

    builder = ReasoningGraphBuilder()

    events = [

        ReasoningEvent(
            event_type="HISTORY_RESPONSE_REQUEST",
            payload={
                "question": "Chest pain"
            },
            source="TEST"
        ),

        ReasoningEvent(
            event_type="INVESTIGATION_RESULT",
            payload={
                "test": "ECG"
            },
            source="TEST"
        ),

        ReasoningEvent(
            event_type="DECISION_ASSESSMENT",
            payload={
                "decision": "NSTEMI"
            },
            source="TEST"
        ),

        ReasoningEvent(
            event_type="OUTCOME_UPDATED",
            payload={
                "status": "DIAGNOSED"
            },
            source="TEST"
        )

    ]


    for event in events:

        builder.process_event(
            event
        )


    graph = builder.graph


    assert len(
        graph.nodes
    ) == 4


    assert len(
        graph.edges
    ) == 3


    assert (
        graph.nodes[0].primitive.value
        == "OBSERVATION"
    )


    assert (
        graph.nodes[1].primitive.value
        == "INVESTIGATION"
    )


    assert (
        graph.nodes[2].primitive.value
        == "DECISION"
    )


    assert (
        graph.nodes[3].primitive.value
        == "OUTCOME"
    )


    assert (
        graph.edges[0].source
        == graph.nodes[0].id
    )


    assert (
        graph.edges[0].target
        == graph.nodes[1].id
    )


    assert (
        graph.edges[1].source
        == graph.nodes[1].id
    )


    assert (
        graph.edges[1].target
        == graph.nodes[2].id
    )


    assert (
        graph.edges[2].source
        == graph.nodes[2].id
    )


    assert (
        graph.edges[2].target
        == graph.nodes[3].id
    )


    print(
        "Reasoning Graph Test Passed"
    )


if __name__ == "__main__":

    test_reasoning_graph_builder()
