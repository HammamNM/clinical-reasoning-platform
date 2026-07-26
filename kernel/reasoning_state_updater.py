class ReasoningStateUpdater:


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

            reasoning_state.active_hypotheses.append(
                action
            )


        elif action.startswith(
            "TREAT_"
        ):

            reasoning_state.performed_treatments.append(
                action
            )
