from simulation.session import ClinicalSession

from decision_engine.engine import DecisionEngine


session = ClinicalSession()


engine = DecisionEngine()


profile = engine.evaluate_decision(
    session,
    "ORDER_UNNECESSARY_CT"
)


print("ACTION:")
print(profile.action)


print("\nASSESSMENTS:")

for assessment in profile.assessments:

    print(
        assessment.dimension,
        assessment.score,
        assessment.explanation
    )
