class OutcomeMapper:


    def __init__(self):

        self.mappings = {}



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

        return self.mappings.get(action)
