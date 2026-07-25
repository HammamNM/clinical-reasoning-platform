from dataclasses import dataclass



@dataclass
class PatternDefinition:

    pattern_id: str

    name: str

    category: str

    description: str



class PatternRegistry:


    def __init__(self):

        self.patterns = {}

        self.register_default_patterns()



    def register(
        self,
        pattern
    ):

        self.patterns[
            pattern.pattern_id
        ] = pattern



    def get(
        self,
        pattern_id
    ):

        return self.patterns.get(
            pattern_id
        )



    def register_default_patterns(
        self
    ):


        self.register(

            PatternDefinition(

                pattern_id="CP-001",

                name="INVESTIGATION_BEFORE_HISTORY",

                category="Information Gathering",

                description=(

                    "Student requested investigations before collecting history."

                )

            )

        )


        self.register(

            PatternDefinition(

                pattern_id="CP-101",

                name="PREMATURE_CLOSURE",

                category="Diagnostic Reasoning",

                description=(

                    "Student accepted diagnosis without adequate confirmation."

                )

            )

        )
