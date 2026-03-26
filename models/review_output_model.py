class ReviewOutput:

    def __init__(self, score, missing, track):
        self.score = score
        self.missing = missing
        self.track = track

    def to_dict(self):
        return {
            "score": self.score,
            "missing": self.missing,
            "track": self.track,
        }