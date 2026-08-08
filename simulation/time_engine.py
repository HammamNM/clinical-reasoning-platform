from kernel.events import ReasoningEvent



class TimeEngine:


    def process_event(
        self,
        event,
        session
    ):


        if event.event_type != "ACTION":

            return None



        session.clock.tick(
            1
        )


        session.state.advance_time(
            1
        )



        return ReasoningEvent(

            event_type="TIME_ADVANCED",

            payload={

                "elapsed_minutes":

                    session.state.elapsed_minutes

            },

            source="TIME_ENGINE"

        )
