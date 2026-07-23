class OutcomeMapper:


    def __init__(self):

        self.mappings = {

            "ORDER_ECG": "ECG_COMPLETED",

            "ORDER_TROPONIN": "TROPONIN_COMPLETED",

            "MAKE_DIAGNOSIS": "DIAGNOSIS_MADE"

        }



    def register(
        self,
        action,
        event
    ):

        self.mappings[action] = event



    def map_action(
        self,
        action
    ):

        return self.mappings.get(
            action
        )
