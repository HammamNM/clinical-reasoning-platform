from backend.case_loader import CaseLoader
from outcome_engine.mapper import OutcomeMapper
from decision_engine.engine import DecisionEngine
from decision_engine.recorder import DecisionRecorder

from outcome_engine.engine import OutcomeEngine
from simulation.timeline import TimelineEngine
from simulation.rules import RuleEngine


class SimulationOrchestrator:

    def __init__(self, session):

        self.session = session

        self.rule_engine = RuleEngine()

        self.timeline_engine = TimelineEngine()

        self.decision_engine = DecisionEngine()

        self.decision_recorder = DecisionRecorder(
            self.decision_engine
        )

        self.outcome_engine = OutcomeEngine()

        self.outcome_mapper = OutcomeMapper()
     
        self.case_loader = CaseLoader()

    def process_student_action(self, action):

        outcome_event = (
            self.outcome_mapper
            .map_action(action)
        )

        if outcome_event:

            self.outcome_engine.process_event(
                outcome_event.event_type,
                self.session.outcome
            )


        self.rule_engine.process_action(
            action,
            self.session.state
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

            self.session.event_stream.add(event)


        self.rule_engine.events.clear()


        self.session.clock.advance(1)


        timeline_events = (
            self.timeline_engine
            .get_events_at_time(
                self.session.clock.get_time()
            )
        )


        for event in timeline_events:

            self.session.event_stream.add(event)

    def load_case(
        self,
        filepath
    ):

        self.session.active_case = (
            self.case_loader.load_case(
                filepath
            )
        )
