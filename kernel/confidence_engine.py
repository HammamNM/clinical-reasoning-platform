class ConfidenceEngine:


    def increase(
        self,
        hypothesis,
        amount
    ):

        hypothesis.confidence += amount


        if hypothesis.confidence > 1.0:

            hypothesis.confidence = 1.0



    def decrease(
        self,
        hypothesis,
        amount
    ):

        hypothesis.confidence -= amount


        if hypothesis.confidence < 0.0:

            hypothesis.confidence = 0.0



    def update_from_evidence(
        self,
        hypothesis,
        evidence
    ):


        if hypothesis.name in evidence.supports:


            self.increase(

                hypothesis,

                evidence.strength

            )



        if hypothesis.name in evidence.contradicts:


            self.decrease(

                hypothesis,

                evidence.strength

            )
