from kernel.query_engine import QueryEngine
from kernel.models import PrimitiveType



class PrematureClosureDetector:


    def detect(
        self,
        reasoning_graph
    ):

        query = QueryEngine(
            reasoning_graph
        )


        detected = []


        decisions = query.nodes_by_primitive(
            PrimitiveType.DECISION
        )


        investigations = query.nodes_by_primitive(
            PrimitiveType.INVESTIGATION
        )



        # إذا كان هناك قرار بدون أي تحقيقات سابقة

        if len(investigations) == 0:


            for decision in decisions:


                detected.append({

                    "pattern_id":
                        "CP-202",


                    "name":
                        "Premature Closure",


                    "decision":
                        decision.content,


                    "reason":
                        "Decision made before sufficient evidence collection"

                })


        return detected
