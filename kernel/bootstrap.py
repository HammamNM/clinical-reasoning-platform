from kernel.runtime import KernelRuntime

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


class KernelBootstrap:


    def create_runtime(
        self,
        clinical_session
    ):


        session_adapter = (
            ClinicalSessionAdapter(
                clinical_session
            )
        )


        runtime = KernelRuntime(
            session_adapter
        )


        runtime.register_engine(

            DecisionEngineAdapter(
                DecisionEngine()
            )

        )


        runtime.register_engine(

            OutcomeEngineAdapter(
                OutcomeEngine(),
                OutcomeMapper()
            )

        )


        runtime.register_engine(

            InvestigationEngineAdapter(
                InvestigationEngine()
            )

        )


        runtime.register_engine(

            EvidenceEngine()

        )


        runtime.register_engine(

            TransitionEngine()

        )


        return runtime
