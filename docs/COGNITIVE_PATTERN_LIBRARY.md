# Cognitive Pattern Library


## Information Gathering Patterns


---

## CP-001

### Name
INVESTIGATION_BEFORE_HISTORY


### Category
Information Gathering


### Description

Student requests investigations before collecting sufficient clinical information.


### Evidence

- INVESTIGATION_RESULT event appears before HISTORY_RESPONSE_REQUEST event.


### Cognitive Signal

Reduced information gathering behavior.


### Related Metrics

- Information Gathering Score
- Safety Score


### Future Recommendation

Encourage structured history collection before ordering investigations.


---

## CP-002

### Name
MISSING_HISTORY_ELEMENTS


### Category
Information Gathering


### Description

Student completes a decision without collecting key available history information.


### Evidence

- Decision event occurs.
- Required history events are missing.


### Cognitive Signal

Incomplete problem representation.


### Related Metrics

- Clinical Completeness
- Diagnostic Safety


### Future Recommendation

Prompt student to collect missing clinical information.


---


# Diagnostic Reasoning Patterns


---

## CP-101

### Name
PREMATURE_CLOSURE


### Category
Diagnostic Reasoning


### Description

Student accepts an initial diagnosis without adequate confirmation.


### Evidence

- Diagnosis made early.
- No supporting investigation.
- No alternative hypothesis considered.


### Cognitive Signal

Reduced diagnostic flexibility.


### Related Metrics

- Diagnostic Flexibility Score
- Premature Closure Index


### Future Recommendation

Encourage consideration of alternative diagnoses before final decision.


---


## CP-102

### Name
ANCHORING


### Category
Diagnostic Reasoning


### Description

Student remains attached to an early clue despite conflicting evidence.


### Evidence

- Early hypothesis persists.
- Contradictory events are ignored.


### Cognitive Signal

Excessive dependence on initial information.


### Related Metrics

- Anchoring Index


### Future Recommendation

Encourage reassessment after new evidence appears.
