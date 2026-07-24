from kernel.runtime import KernelRuntime
from kernel.session import KernelSession


from kernel.adapters.decision_adapter import (
    DecisionEngineAdapter
)

from kernel.adapters.outcome_adapter import (
    OutcomeEngineAdapter
)

from kernel.adapters.investigation_adapter import (
    InvestigationEngineAdapter
)


from decision_engine.engine import DecisionEngine
from outcome_engine.engine import OutcomeEngine
from outcome_engine.mapper import OutcomeMapper
from simulation.investigation_engine import InvestigationEngine



class KernelBootstrap:


    def create_runtime(
        self
    ):

        session = KernelSession()


        runtime = KernelRuntime(
            session
        )


        decision_adapter = (
            DecisionEngineAdapter(
                DecisionEngine()
            )
        )


        outcome_adapter = (
            OutcomeEngineAdapter(
                OutcomeEngine(),
                OutcomeMapper()
            )
        )


        investigation_adapter = (
            InvestigationEngineAdapter(
                InvestigationEngine()
            )
        )


        runtime.register_engine(
            decision_adapter
        )


        runtime.register_engine(
            outcome_adapter
        )


        runtime.register_engine(
            investigation_adapter
        )


        return runtime
