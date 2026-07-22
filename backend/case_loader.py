import json


class CaseLoader:


    def load_case(
        self,
        filepath
    ):

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as file:

            case = json.load(file)


        return case
