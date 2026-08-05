from kernel.hypothesis_manager import (
    HypothesisManager
)


class ReasoningStateUpdater:


    def __init__(self):

        self.hypothesis_manager = (
            HypothesisManager()
        )


    def update(
        self,
        reasoning_state,
        event
    ):

        payload = getattr(
            event,
            "payload",
            {}
        )


        action = payload.get(
            "action"
        )


        if action is None:

            return


        if action.startswith(
            "ASK_"
        ):

            reasoning_state.collected_information.append(
                action
            )


        elif action.startswith(
            "ORDER_"
        ):

            reasoning_state.ordered_investigations.append(
                action
            )


        elif action.startswith(
            "DIAGNOSIS_"
        ):

            hypothesis = self.hypothesis_manager.find(

                reasoning_state,

                action

            )


            if hypothesis is None:

                self.hypothesis_manager.create(

                    reasoning_state,

                    action,

                    trigger=action

                )


        elif action.startswith(
            "CONFIRM_"
        ):

            hypothesis_name = action.replace(
                "CONFIRM_",
                "DIAGNOSIS_"
            )


            hypothesis = self.hypothesis_manager.find(

                reasoning_state,

                hypothesis_name

            )


            if hypothesis is not None:

                self.hypothesis_manager.confirm(
                    hypothesis
                )

                reasoning_state.confirmed_hypotheses.append(
                    hypothesis
                )


        elif action.startswith(
            "REJECT_"
        ):

            hypothesis_name = action.replace(
                "REJECT_",
                "DIAGNOSIS_"
            )


            hypothesis = self.hypothesis_manager.find(

                reasoning_state,

                hypothesis_name
            )


            if hypothesis is not None:

                self.hypothesis_manager.reject(

                    reasoning_state,

                    hypothesis

                )


        elif action.startswith(
            "TREAT_"
        ):

            reasoning_state.performed_treatments.append(
                action
            )
