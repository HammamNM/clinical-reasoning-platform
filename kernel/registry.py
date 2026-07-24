class EngineRegistry:


    def __init__(self):

        self.engines = []



    def register(
        self,
        engine
    ):

        self.engines.append(
            engine
        )



    def get_engines(
        self
    ):

        return list(
            self.engines
        )



    def dispatch(
        self,
        event,
        session
    ):

        generated_events = []


        for engine in self.engines:

            if hasattr(
                engine,
                "process_event"
            ):

                result = engine.process_event(
                    event,
                    session
                )


                if result:

                    if isinstance(
                        result,
                        list
                    ):

                        generated_events.extend(
                            result
                        )

                    else:

                        generated_events.append(
                            result
                        )


        return generated_events
