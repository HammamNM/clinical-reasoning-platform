class EventBridge:


    def __init__(self):

        self.events = []


    def collect(
        self,
        event
    ):

        self.events.append(
            event
        )


    def collect_many(
        self,
        events
    ):

        self.events.extend(
            events
        )


    def get_events(
        self
    ):

        return self.events


    def clear(
        self
    ):

        self.events.clear()
