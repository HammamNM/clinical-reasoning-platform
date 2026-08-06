from kernel.reasoning_transition import (
    TransitionRecorder
)


class TransitionEngine:


    def __init__(self):

        self.recorders = {}



    def process_event(
        self,
        event,
        session
    ):

        if not hasattr(
            session,
            "reasoning_state"
        ):

            return None


        action = event.payload.get(
            "action"
        )


        if action is None:

            return None


        from_state = (
            self.get_previous_state(
                session
            )
        )


        to_state = (
            self.detect_state(
                action
            )
        )


        if to_state is None:

            return None


        session.reasoning_state.transitions.record(

            from_state,

            to_state,

            action

        )



    def detect_state(
        self,
        action
    ):

        if action.startswith(
            "ASK_"
        ):

            return "OBSERVATION"


        if action.startswith(
            "DIAGNOSIS_"
        ):

            return "HYPOTHESIS"


        if action.startswith(
            "ORDER_"
        ):

            return "INVESTIGATION"


        if action.startswith(
            "TREAT_"
        ):

            return "DECISION"


        if action.startswith(
            "CONFIRM_"
        ):

            return "CONFIRMATION"


        if action.startswith(
            "REJECT_"
        ):

            return "REJECTION"


        return None



    def get_previous_state(
        self,
        session
    ):

        transitions = (
            session.reasoning_state
            .transitions
            .transitions
        )


        if not transitions:

            return "START"


        return transitions[-1].to_state
