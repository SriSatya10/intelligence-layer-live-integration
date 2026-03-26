# Handover Notes — Intelligence Layer Integration

## Purpose

This module generates the next task automatically from review output.

It is integrated into the live pipeline and runs without simulation.


## How the System Works

Flow:

submission
→ ReviewEngine
→ ReviewOutput
→ IntelligenceAdapter
→ TaskIntelligenceEngine
→ ContractValidator
→ response


## Main Files

review_engine/review_engine.py  
orchestrator/review_orchestrator.py  
adapter/intelligence_adapter.py  
engine/task_intelligence_engine.py  
validator/contract_validator.py  
pipeline_test.py


## How to Run

Run full pipeline test:

python pipeline_test.py


## Expected Output

FAIL → correction task  
BORDERLINE → reinforcement task  
PASS → next level task


## Failure Safety

If intelligence fails, fallback task is returned.


## Contract Rules

next_task must contain:

title  
objective  
focus_area  
difficulty  
expected_deliverables


## Deterministic Behavior

Same input always produces same next task.


## Notes for Next Developer

Do not modify contract fields.

Do not remove validator.

Do not bypass orchestrator.

Always run pipeline_test before changes.


## FAQ

Q: Where is intelligence logic?
A: engine/task_intelligence_engine.py

Q: Where is pipeline?
A: orchestrator/review_orchestrator.py

Q: Where is validation?
A: validator/contract_validator.py

Q: How to test?
A: run pipeline_test.py