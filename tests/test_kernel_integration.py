from kernel.bootstrap import KernelBootstrap

from simulation.session import ClinicalSession


def test_full_kernel_flow():

    session = ClinicalSession(

        scenario_id="TEST_001"

    )


    runtime = KernelBootstrap().create_runtime(
        session
    )


    runtime.publish(

        runtime.create_event(

            "ASK_CHEST_PAIN"

        )

    )


    runtime.run_cycle()


    runtime.publish(

        runtime.create_event(

            "DIAGNOSIS_NSTEMI"

        )

    )


    runtime.run_cycle()



    graph = runtime.graph_builder.graph


    assert len(
        graph.nodes
    ) == 2


    assert len(
        graph.edges
    ) == 1



    transitions = (

        runtime.session

        .reasoning_state

        .transitions

        .transitions

    )


    assert len(
        transitions
    ) > 0
