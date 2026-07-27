class PerformanceAnalyzer:


    def calculate_average_score(
        self,
        session
    ):

        if not session.decision_history:

            return 0.0


        total = sum(
            profile.total_score
            for profile in session.decision_history
        )


        return (
            total
            /
            len(session.decision_history)
        )


    def calculate_dimension_scores(
        self,
        session
    ):

        dimensions = {}


        for profile in session.decision_history:

            for assessment in profile.assessments:

                if assessment.dimension not in dimensions:

                    dimensions[
                        assessment.dimension
                    ] = []


                dimensions[
                    assessment.dimension
                ].append(
                    assessment.score
                )


        averages = {}


        for dimension, scores in dimensions.items():

            averages[dimension] = (

                sum(scores)

                /

                len(scores)

            )


        return averages


    def calculate_progress_trend(
        self,
        session
    ):

        scores = [

            profile.total_score

            for profile in session.decision_history

        ]


        if len(scores) < 2:

            return "INSUFFICIENT_DATA"


        first_average = (

            sum(scores[:len(scores)//2])

            /

            len(scores[:len(scores)//2])

        )


        second_average = (

            sum(scores[len(scores)//2:])

            /

            len(scores[len(scores)//2:])

        )


        difference = (

            second_average

            -

            first_average

        )


        if difference >= 1:

            return "IMPROVING"


        elif difference <= -1:

            return "DECLINING"


        return "STABLE"


    def analyze(
        self,
        session
    ):

        return {

            "average_score":

                self.calculate_average_score(
                    session
                ),

            "dimensions":

                self.calculate_dimension_scores(
                    session
                ),

            "trend":

                self.calculate_progress_trend(
                    session
                )

        }
