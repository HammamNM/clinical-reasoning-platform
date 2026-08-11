from kernel.runtime import (
    KernelRuntime
)

from kernel.adapters.session_adapter import (
    ClinicalSessionAdapter
)

from kernel.evidence_engine import (
    EvidenceEngine
)

from kernel.adapters.decision_adapter import (
    DecisionEngineAdapter
)

from kernel.adapters.outcome_adapter import (
    OutcomeEngineAdapter
)

from kernel.adapters.investigation_adapter import (
    InvestigationEngineAdapter
)

from kernel.adapters.scenario_adapter import (
    ScenarioEngineAdapter
)

from decision_engine.engine import (
    DecisionEngine
)

from outcome_engine.engine import (
    OutcomeEngine
)

from outcome_engine.mapper import (
    OutcomeMapper
)

from simulation.investigation_engine import (
    InvestigationEngine
)

from kernel.transition_engine import (
    TransitionEngine
)

from kernel.scenario_engine import (
    ScenarioEngine
)


class KernelBootstrap:


    def create_runtime(
        self,
        clinical_session,
        scenario=None
    ):

        session_adapter = (
            ClinicalSessionAdapter(
                clinical_session
            )
        )


        runtime = KernelRuntime(
            session_adapter
        )


        # -------------------------------------------------
        # Register engines
        # -------------------------------------------------


        runtime.register_engine(

            InvestigationEngineAdapter(
                InvestigationEngine()
            ),

            priority=20

        )


        runtime.register_engine(

            EvidenceEngine(),

            priority=30

        )


        runtime.register_engine(

            DecisionEngineAdapter(
                DecisionEngine()
            ),

            priority=40

        )


        runtime.register_engine(

            OutcomeEngineAdapter(
                OutcomeEngine(),
                OutcomeMapper()
            ),

            priority=50

        )


        runtime.register_engine(

            TransitionEngine(),

            priority=60

        )


        # -------------------------------------------------
        # Scenario Engine
        # -------------------------------------------------


        if scenario is not None:

            scenario_engine = (
                ScenarioEngine(
                    scenario
                )
            )


            runtime.set_scenario_engine(

                scenario_engine

            )


            runtime.register_engine(

                ScenarioEngineAdapter(
                    scenario_engine
                ),

                priority=10

            )


        # -------------------------------------------------
        # Initialize runtime
        # -------------------------------------------------


        runtime.initialize()


        return runtime
