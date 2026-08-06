class EventDispatcher:


    def __init__(
        self,
        runtime
    ):

        self.runtime = runtime


    def dispatch(
        self,
        event
    ):

        self.runtime.session.event_stream.publish(
            event
        )


        self.runtime.graph_builder.process_event(
            event
        )


        self.runtime.reasoning_updater.update(

            self.runtime.session.reasoning_state,

            event

        )


        generated_events = (

            self.runtime.registry.dispatch(

                event,

                self.runtime.session

            )

        )


        for generated_event in generated_events:

            self.runtime.publish(

                generated_event

            )
