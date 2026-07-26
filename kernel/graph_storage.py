import json

from kernel.graph_serializer import (
    GraphSerializer
)


class GraphStorage:


    def __init__(self):

        self.serializer = (
            GraphSerializer()
        )


    def save(

        self,

        graph,

        filepath

    ):

        data = self.serializer.export(
            graph
        )


        with open(

            filepath,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                data,

                file,

                indent=4

            )
