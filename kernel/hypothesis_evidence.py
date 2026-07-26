from dataclasses import dataclass, field


@dataclass
class EvidenceLink:

    hypothesis_name: str

    evidence_type: str

    evidence: dict

    effect: str

    weight: float



class HypothesisEvidenceLinker:


    def link_support(

        self,

        hypothesis,

        evidence,

        weight=0.15

    ):

        link = EvidenceLink(

            hypothesis_name=hypothesis.name,

            evidence_type="SUPPORT",

            evidence=evidence,

            effect="INCREASE_CONFIDENCE",

            weight=weight

        )


        hypothesis.supporting_evidence.append(
            link
        )


        return link



    def link_contradiction(

        self,

        hypothesis,

        evidence,

        weight=0.20

    ):

        link = EvidenceLink(

            hypothesis_name=hypothesis.name,

            evidence_type="CONTRADICTION",

            evidence=evidence,

            effect="DECREASE_CONFIDENCE",

            weight=weight

        )


        hypothesis.contradicting_evidence.append(
            link
        )


        return link
