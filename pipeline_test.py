from orchestrator.review_orchestrator import ReviewOrchestrator


def run_tests():

    orchestrator = ReviewOrchestrator()

    # ---------- FAIL CASE ----------
    submission_fail = {
        "score": 20,
        "missing": ["logic"],
        "track": "backend",
    }

    print("FAIL CASE")
    print(orchestrator.run_pipeline(submission_fail))
    print()

    # ---------- BORDERLINE CASE ----------
    submission_borderline = {
        "score": 55,
        "missing": [],
        "track": "backend",
    }

    print("BORDERLINE CASE")
    print(orchestrator.run_pipeline(submission_borderline))
    print()

    # ---------- PASS CASE ----------
    submission_pass = {
        "score": 85,
        "missing": [],
        "track": "backend",
    }

    print("PASS CASE")
    print(orchestrator.run_pipeline(submission_pass))
    print()


if __name__ == "__main__":
    run_tests()