from kernel.hypothesis_manager import (
    HypothesisManager
)

self.hypothesis_manager = (
    HypothesisManager()
)
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

            from kernel.hypothesis import Hypothesis

            
        self.hypothesis_manager.create(

            reasoning_state,

            action,

            trigger=action

        )
            Hypothesis(

            name=action,

            confidence=0.50,

            created_by=action

        )

                  ) 
            


        elif action.startswith(
            "TREAT_"

        ):

            reasoning_state.performed_treatments.append(
                action
            )
