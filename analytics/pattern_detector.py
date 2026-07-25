from collections import Counter


class PatternDetector:


    def analyze(
        self,
        event_bridge
    ):

        events = (
            event_bridge.get_events()
        )


        counter = Counter()


        for event in events:

            counter[
                event.event_type
            ] += 1


        return {

            "event_counts": dict(counter),

            "total_events": len(events)

        }
