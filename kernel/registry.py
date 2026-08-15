class EngineRegistry:


    def __init__(
        self
    ):

        self.engines = []


    def register(
        self,
        engine,
        priority=0
    ):

        self.engines.append(

            (
                priority,
                engine
            )

        )

        self.engines.sort(

            key=lambda item: item[0]

        )


    def get_engines(
        self
    ):

        return [

            engine

            for priority, engine
            in self.engines

        ]


    def dispatch(
        self,
        event,
        session
    ):

        generated_events = []


        for priority, engine in self.engines:

            if not hasattr(
                engine,
                "process_event"
            ):

                continue


            result = engine.process_event(

                event,

                session

            )


            if result is None:

                continue


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
