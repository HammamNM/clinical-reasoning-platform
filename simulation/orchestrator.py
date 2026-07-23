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

        if action in INVESTIGATION_ACTIONS:

            self.investigation_engine.process_action(
                action,
                self.session.active_case,
                self.session.event_stream
            )

        elif action in THERAPEUTIC_ACTIONS:

            self.rule_engine.process_action(
                action,
                self.session.state
            )

        elif action in DIAGNOSTIC_ACTIONS:

            self.rule_engine.process_action(
                action,
                self.session.state
            )

        elif action in HISTORY_ACTIONS:

            self.session.event_stream.add(
                {
                    "event_type": "HISTORY_RESPONSE_REQUEST",
                    "content": action
                }
            )


    def process_student_action(
        self,
        action
    ):

    print("ACTION RECEIVED:", action)
        
        self.dispatch_action(
            action
        )

        outcome_event = (
            self.outcome_mapper.map_action(
                action
            )
        )

        if outcome_event:

            self.outcome_engine.process_event(
                outcome_event.event_type,
                self.session.outcome
            )

        decision_profile = (
            self.decision_recorder.record(
                self.session,
                action
            )
        )

        self.session.event_stream.add(
            {
                "event_type": "DECISION_PROFILE",
                "content": decision_profile
            }
        )

        for event in self.rule_engine.events:

            self.session.event_stream.add(
                event
            )

        self.rule_engine.events.clear()

        self.session.clock.advance(1)

        timeline_events = (
            self.timeline_engine.get_events_at_time(
                self.session.clock.get_time()
            )
        )

        for event in timeline_events:

            self.session.event_stream.add(
                event
            )


    def run_session(
        self,
        actions
    ):

        for action in actions:

            self.process_student_action(
                action
            )

        return self.session
