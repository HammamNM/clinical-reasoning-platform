from kernel.events import (
    ReasoningEvent
)

from kernel.scenario_state import (
    ScenarioState
)


class ScenarioEngine:


    def __init__(
        self,
        scenario
    ):

        self.scenario = scenario

        self.state = ScenarioState()


    def initialize(
        self,
        session
    ):

        session.scenario_id = (
            self.scenario.scenario_id
        )


        session.state.update(

            self.scenario.initial_state

        )


        self.state.variables = dict(

            self.scenario.initial_state

        )


        self.state.current_stage = (
            self.scenario.metadata.get(

                "initial_stage",

                "INITIAL"

            )
        )


        self.state.ended = False

        self.state.outcome_id = ""

        self.state.completed_actions.clear()

        self.state.completed_investigations.clear()

        self.state.triggered_events.clear()


        return ReasoningEvent(

            event_type="SCENARIO_INITIALIZED",

            source="SCENARIO_ENGINE",

            payload={

                "scenario_id":
                    self.scenario.scenario_id,

                "title":
                    self.scenario.title,

                "patient":
                    self.scenario.patient,

                "stage":
                    self.state.current_stage

            }

        )


    def process_action(
        self,
        action,
        session
    ):

        if self.state.ended:

            return None


        if action in self.state.completed_actions:

            return None


        action_config = (
            self.get_action_config(
                action
            )
        )


        if action_config is None:

            return None


        if not self.is_action_available(
            action_config
        ):

            return None


        self.state.completed_actions.append(
            action
        )


        generated_events = []


        self.apply_state_changes(
            action_config
        )


        event = self.create_action_event(

            action,

            action_config

        )


        if event is not None:

            generated_events.append(
                event
            )


        investigation_id = (
            action_config.get(
                "investigation_id"
            )
        )


        if investigation_id:

            event = self.complete_investigation(

                investigation_id,

                session

            )


            if event is not None:

                generated_events.append(
                    event
                )


        next_stage = (
            action_config.get(
                "next_stage"
            )
        )


        if next_stage:

            self.state.current_stage = (
                next_stage
            )


        outcome_id = (
            action_config.get(
                "outcome_id"
            )
        )


        if outcome_id:

            event = self.trigger_outcome(

                outcome_id,

                session

            )


            if event is not None:

                generated_events.append(
                    event
                )


        return generated_events


    def get_action_config(
        self,
        action
    ):

        actions = (
            self.scenario.metadata.get(
                "actions",
                {}
            )
        )


        return actions.get(
            action
        )


    def is_action_available(
        self,
        action_config
    ):

        required_stage = (
            action_config.get(
                "stage"
            )
        )


        if (

            required_stage is not None

            and

            required_stage
            != self.state.current_stage

        ):

            return False


        required_actions = (
            action_config.get(
                "requires_actions",
                []
            )
        )


        for required_action in (
            required_actions
        ):

            if required_action not in (
                self.state.completed_actions
            ):

                return False


        required_investigations = (
            action_config.get(
                "requires_investigations",
                []
            )
        )


        for investigation_id in (
            required_investigations
        ):

            if investigation_id not in (
                self.state.completed_investigations
            ):

                return False


        return True


    def apply_state_changes(
        self,
        action_config
    ):

        changes = (
            action_config.get(
                "state_changes",
                {}
            )
        )


        self.state.variables.update(
            changes
        )


    def create_action_event(
        self,
        action,
        action_config
    ):

        event_type = action_config.get(
            "event_type"
        )


        if event_type is None:

            return None


        self.state.triggered_events.append(
            action
        )


        return ReasoningEvent(

            event_type=event_type,

            source="SCENARIO_ENGINE",

            payload={

                "action":
                    action,

                "result":
                    action_config.get(
                        "result"
                    ),

                "state":
                    dict(
                        self.state.variables
                    )

            }

        )


    def complete_investigation(
        self,
        investigation_id,
        session
    ):

        if investigation_id in (
            self.state.completed_investigations
        ):

            return None


        investigation = (
            self.scenario.investigations.get(
                investigation_id
            )
        )


        if investigation is None:

            return None


        self.state.completed_investigations.append(
            investigation_id
        )


        return ReasoningEvent(

            event_type="INVESTIGATION_RESULT",

            source="SCENARIO_ENGINE",

            payload={

                "investigation_id":
                    investigation_id,

                "result":
                    investigation

            }

        )


    def trigger_outcome(
        self,
        outcome_id,
        session
    ):

        outcome = (
            self.scenario.outcomes.get(
                outcome_id
            )
        )


        if outcome is None:

            return None


        self.state.ended = True

        self.state.outcome_id = (
            outcome_id
        )

        self.state.current_stage = "ENDED"


        return ReasoningEvent(

            event_type="OUTCOME_UPDATED",

            source="SCENARIO_ENGINE",

            payload={

                "outcome_id":
                    outcome_id,

                "outcome":
                    outcome

            }

        )


    def get_available_actions(
        self
    ):

        if self.state.ended:

            return []


        available = []


        actions = (
            self.scenario.metadata.get(
                "actions",
                {}
            )
        )


        for action, config in (
            actions.items()
        ):

            if action in (
                self.state.completed_actions
            ):

                continue


            if self.is_action_available(
                config
            ):

                available.append(
                    action
                )


        return available


    def get_investigation(
        self,
        investigation_id
    ):

        return self.scenario.investigations.get(
            investigation_id
        )


    def get_outcome(
        self,
        outcome_id
    ):

        return self.scenario.outcomes.get(
            outcome_id
        )
