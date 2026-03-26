from models.next_task_model import NextTask
from engine.decision_rules import DecisionRules
from engine.architecture_guard import ArchitectureGuard


class TaskIntelligenceEngine:

    def __init__(self):
        self.rules = DecisionRules()
        self.guard = ArchitectureGuard()

    def generate_next_task(self, review_output) -> dict:
        """
        Input:
            review_output from real review engine

        Output:
            next_task dict compatible with API
        """

        # ---- Safe mapping (supports dict or object) ----

        if isinstance(review_output, dict):
            data = review_output
        else:
            # convert object to dict if needed
            data = review_output.__dict__

        # Step 1 — decision rules
        task_data = self.rules.decide(data)

        # Step 2 — architecture guard
        task_data = self.guard.ensure_valid(
            task_data,
            data,
        )

        # Step 3 — convert to model
        next_task = NextTask(**task_data)

        return next_task.to_dict()