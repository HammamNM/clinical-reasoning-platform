from kernel.events import EventStream


class EventBridge:

    def __init__(self):
        self.stream = EventStream()


    def collect(self, events):

        for event in events:
            self.stream.add(event)


    def get_events(self):

        return self.stream.get_all()

class EventBridge:


    def process_events(
        self,
        session
    ):

        events = (
            session.event_stream.events
        )


        return events
