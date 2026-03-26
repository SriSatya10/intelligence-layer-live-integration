from models.review_output_model import ReviewOutput


class ReviewEngine:

    def evaluate_submission(self, submission):
        """
        Simulates real review engine

        In real system this comes from scoring layer
        """

        # simple logic for now
        score = submission.get("score", 0)
        missing = submission.get("missing", [])
        track = submission.get("track", "general")

        review_output = ReviewOutput(
            score=score,
            missing=missing,
            track=track,
        )

        return review_output