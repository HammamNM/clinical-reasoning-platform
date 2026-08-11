class EngineRegistry:


    def __init__(self):

        self.engines = []


    def register(
        self,
        engine,
        priority=100
    ):

        if not hasattr(
            engine,
            "process_event"
        ):

            raise TypeError(
                "Engine must implement process_event"
            )


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

            for _, engine in self.engines

        ]


    def dispatch(
        self,
        event,
        session
    ):

        from kernel.events import (
            ReasoningEvent
        )


        generated_events = []


        for _, engine in self.engines:

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

                for generated_event in result:

                    if not isinstance(
                        generated_event,
                        ReasoningEvent
                    ):

                        raise TypeError(

                            "Engine generated an invalid event: "

                            f"{type(generated_event).__name__}"

                        )


                    generated_events.append(
                        generated_event
                    )


            else:

                if not isinstance(
                    result,
                    ReasoningEvent
                ):

                    raise TypeError(

                        "Engine generated an invalid event: "

                        f"{type(result).__name__}"

                    )


                generated_events.append(
                    result
                )


        return generated_events
