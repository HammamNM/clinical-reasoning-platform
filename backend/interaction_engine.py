import json

from kernel.events import ReasoningEvent


class InteractionEngine:

    def __init__(self, case_path):

        with open(case_path, "r", encoding="utf-8") as file:
            self.case = json.load(file)

        self.events = []

    def show_stage(self, stage_number):

        for stage in self.case["stages"]:

            if stage["stage"] == stage_number:

                print("\nCASE INFORMATION")
                print(stage["information"])

                print("\nAVAILABLE CHOICES")

                for i, choice in enumerate(stage["choices"], start=1):
                    print(f"{i}. {choice}")

                return stage

        return None

    def record_choice(self, choice):

        event = ReasoningEvent(
            event_id=f"E{len(self.events)+1}",
            event_type="CHOICE",
            content=choice
        )

        self.events.append(event)

        print("\nRecorded:")
        print(choice)

    def show_events(self):

        print("\nEvents")

        for event in self.events:
            print(event)
