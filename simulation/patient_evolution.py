from kernel.events import ReasoningEvent



class PatientEvolutionEngine:


    def process_time(
        self,
        session
    ):


        elapsed = session.state.elapsed_minutes


        events = []



        if elapsed >= 10 and not session.state.troponin_visible:


            session.state.pain_level += 1


            events.append(

                ReasoningEvent(

                    event_type="PATIENT_CHANGED",

                    payload={

                        "change":

                            "Pain increased due to delayed management"

                    },

                    source="PATIENT_EVOLUTION"

                )

            )



        if elapsed >= 20:


            session.outcome.status = "WORSENING"

            session.outcome.severity = 3


            events.append(

                ReasoningEvent(

                    event_type="OUTCOME_UPDATED",

                    payload={

                        "status":

                            "WORSENING",

                        "severity":

                            3

                    },

                    source="PATIENT_EVOLUTION"

                )

            )



        return events
