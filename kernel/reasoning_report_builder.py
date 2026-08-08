from kernel.reasoning_report import (
    ReasoningReport,
    HypothesisReport
)

from kernel.query_engine import (
    QueryEngine
)


class ReasoningReportBuilder:


    def build(
        self,
        session,
        graph
    ):

        query = QueryEngine(
            graph
        )


        session_id = getattr(
            session,
            "session_id",
            ""
        )


        report = ReasoningReport(

            session_id=session_id

        )


        reasoning_state = getattr(
            session,
            "reasoning_state",
            None
        )


        if reasoning_state is not None:

            for hypothesis in (
                reasoning_state.hypotheses
            ):

                supporting = [

                    evidence.content

                    for evidence in (
                        hypothesis.supporting_evidence
                    )

                ]


                contradicting = [

                    evidence.content

                    for evidence in (
                        hypothesis.contradicting_evidence
                    )

                ]


                history = [

                    {

                        "previous": update.previous,

                        "change": update.change,

                        "current": update.current,

                        "reason": update.reason

                    }

                    for update in (
                        hypothesis.confidence_history
                    )

                ]


                hypothesis_report = HypothesisReport(

                    name=hypothesis.name,

                    confidence=hypothesis.confidence,

                    status=hypothesis.status,

                    supporting_evidence=supporting,

                    contradicting_evidence=contradicting,

                    confidence_history=history

                )


                report.hypotheses.append(
                    hypothesis_report
                )


        report.confirmed_hypotheses = [

            node.id

            for node in (
                query.confirmed_hypotheses()
            )

        ]


        report.rejected_hypotheses = [

            node.id

            for node in (
                query.rejected_hypotheses()
            )

        ]


        report.reasoning_nodes = [

            {

                "id": node.id,

                "primitive": node.primitive.value,

                "content": node.content

            }

            for node in graph.nodes

        ]


        report.reasoning_edges = [

            {

                "source": edge.source,

                "target": edge.target,

                "relation": edge.relation.value

            }

            for edge in graph.edges

        ]


        report.reasoning_path = [

            node.id

            for node in graph.nodes

        ]


        if hasattr(
            session,
            "evidence"
        ):

            report.evidence = [

                {

                    "id": evidence.evidence_id,

                    "source": evidence.source,

                    "content": evidence.content,

                    "strength": evidence.strength,

                    "supports": evidence.supports,

                    "contradicts": evidence.contradicts

                }

                for evidence in session.evidence

            ]


        return report
