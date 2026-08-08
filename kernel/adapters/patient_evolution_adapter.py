class PatientEvolutionAdapter:


    def __init__(
        self,
        evolution_engine
    ):

        self.evolution_engine = evolution_engine



    def process_event(
        self,
        event,
        session
    ):


        if event.event_type != "TIME_ADVANCED":

            return None



        return self.evolution_engine.process_time(
            session
        )
