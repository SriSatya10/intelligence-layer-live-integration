from engine.task_intelligence_engine import TaskIntelligenceEngine


class IntelligenceAdapter:

    def __init__(self):
        self.engine = TaskIntelligenceEngine()

    def process(self, review_output):
        """
        Called by orchestrator after review_engine

        Input:
            review_output (real ReviewOutput object)

        Output:
            next_task dict (contract safe)
        """

        if review_output is None:
            raise ValueError("review_output is required")

        # call intelligence engine
        next_task = self.engine.generate_next_task(
            review_output
        )

        if not isinstance(next_task, dict):
            raise TypeError("next_task must be dict")

        return next_task