from simulation.actions import (
    INVESTIGATION_ACTIONS,
    THERAPEUTIC_ACTIONS,
    DIAGNOSTIC_ACTIONS,
    HISTORY_ACTIONS
)

from simulation.investigation_engine import InvestigationEngine
from simulation.timeline import TimelineEngine
from simulation.rules import RuleEngine

from backend.case_loader import CaseLoader

from decision_engine.engine import DecisionEngine
from decision_engine.recorder import DecisionRecorder

from outcome_engine.engine import OutcomeEngine
from outcome_engine.mapper import OutcomeMapper


class SimulationOrchestrator:

    def __init__(
        self,
        session
    ):

        self.session = session

        self.case_loader = CaseLoader()

        self.investigation_engine = InvestigationEngine()

        self.rule_engine = RuleEngine()

        self.timeline_engine = TimelineEngine()

        self.decision_engine = DecisionEngine()

        self.decision_recorder = DecisionRecorder(
            self.decision_engine
        )

        self.outcome_engine = OutcomeEngine()

        self.outcome_mapper = OutcomeMapper()


    def load_case(
        self,
        filepath
    ):

        self.session.active_case = (
            self.case_loader.load_case(
                filepath
            )
        )


    def dispatch_action(
        self,
        action
    ):
        pass
