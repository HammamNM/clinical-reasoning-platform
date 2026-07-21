from dataclasses import dataclass


@dataclass
class TimelineEvent:

    trigger_time: int
    event_type: str
    content: str
  
class TimelineEngine:

    def __init__(self):

        self.events = []


    def add_event(self, timeline_event):

        self.events.append(timeline_event)


    def get_events_at_time(self, current_time):

        triggered = []

        for event in self.events:

            if event.trigger_time == current_time:

                triggered.append(event)

        return triggered
