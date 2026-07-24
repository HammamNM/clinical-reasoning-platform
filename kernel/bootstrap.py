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
        self,
        session=None
    ):

        kernel_session = (
            session
            if session
            else KernelSession()
        )


        runtime = KernelRuntime(
            kernel_session
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


        return runtime
