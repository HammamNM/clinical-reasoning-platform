from kernel.reasoning_state import ReasoningState

from kernel.hypothesis_manager import (
    HypothesisManager
)

from analytics.anchoring_detector import (
    AnchoringDetector
)



def test_anchoring_detection():


    state = ReasoningState()


    manager = HypothesisManager()


    detector = AnchoringDetector()



    hypothesis = manager.create(

        state,

        "DIAGNOSIS_NSTEMI",

        trigger="INITIAL_THOUGHT"

    )


    manager.add_supporting_evidence(

        hypothesis,

        {
            "finding": "CHEST_PAIN"
        }

    )


    hypothesis.confidence = 0.80



    manager.add_contradicting_evidence(

        hypothesis,

        {
            "finding": "NORMAL_TROPONIN"
        }

    )


    patterns = detector.detect(
        state
    )


    assert len(patterns) == 1


    assert patterns[0]["pattern_id"] == (
        "CP-201"
    )
