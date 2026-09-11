# Intelligence Layer Handover State
## System Purpose
To generate the next task automatically based on the review output from the scoring engine, replacing the manual task assignment process in a fully deterministic way.

## Current State
Functioning in isolation. Components (`task_intelligence_engine.py`, `decision_rules.py`, `architecture_guard.py`) are implemented and testable via `pipeline_test.py`.

## Component-by-component explanation
- **task_intelligence_engine.py**: The orchestrator that takes input, applies rules, checks guards, and outputs a task.
- **decision_rules.py**: The deterministic mapping of review outputs to next actions.
- **architecture_guard.py**: Prevents generated tasks from violating system boundaries.
- **intelligence_adapter.py**: Adapts the output to the required product schema.
- **next_task_model.py**: The data model for the output.
- **task_registry.py**: Contains the predefined templates for tasks to ensure no hallucinatory tasks are created.

## Data flow
Input (ReviewOutput) -> Adapter -> Engine -> Decision Rules -> Architecture Guard -> Engine -> Adapter -> Output (NextTask)

## Input/output examples
**Input**: `{"review_score": 45, "missing_areas": ["security"]}`
**Output**: `{"task_id": "T-102", "task_type": "security_patch", "assigned_to": "auto"}`

## Configuration
No dynamic configuration; rules are currently in code (`decision_rules.py`).

## Dependencies
Python 3.10+. No external databases or APIs required.

## How to run
`python pipeline_test.py` or `python tests/test_intelligence.py`

## How to test
Use the provided `pytest` suite in the `tests/` directory.

## Known failures/limitations
- If input violates schema, the system returns a safe fallback task rather than crashing, but the original intent is lost.
- Simulation-only behavior for the actual product orchestrator connection.

## Integration requirements
Requires Ishan's product orchestrator to call `intelligence_adapter.py`.

## Pending work
- Replace static rule maps with database-backed or JSON-configured rules.
- Real-world integration testing.

## Important design decisions
- Chose complete determinism over AI inference to guarantee repeatability and auditability.
- Added `architecture_guard.py` to ensure boundary safety.

## Date of last verified state
2026-09-11

## Exact Git commit/hash of the handed-over state
4007f16879f6ea952ee10aa88afae4723ee5a098
