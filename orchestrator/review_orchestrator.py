from adapter.intelligence_adapter import IntelligenceAdapter
from review_engine.review_engine import ReviewEngine
from validator.contract_validator import ContractValidator


class ReviewOrchestrator:

    def __init__(self):
        self.review_engine = ReviewEngine()
        self.adapter = IntelligenceAdapter()
        self.validator = ContractValidator()

    def fallback_task(self):
        return {
            "title": "Fallback Task",
            "objective": "Retry submission",
            "focus_area": "general",
            "difficulty": "easy",
            "expected_deliverables": "Resubmit work",
        }

    def run_pipeline(self, submission):

        if submission is None:
            raise ValueError("submission required")

        # Step 1 — review engine
        review_output = self.review_engine.evaluate_submission(
            submission
        )

        try:

            # Step 2 — intelligence
            next_task = self.adapter.process(review_output)

            # Step 3 — validate
            self.validator.validate_next_task(next_task)

        except Exception as e:

            print("INTELLIGENCE FAILED:", e)

            next_task = self.fallback_task()

        response = {
            "review_output": review_output.to_dict(),
            "next_task": next_task,
        }

        return response