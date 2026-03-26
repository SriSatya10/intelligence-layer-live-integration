class ContractValidator:

    REQUIRED_FIELDS = [
        "title",
        "objective",
        "focus_area",
        "difficulty",
        "expected_deliverables",
    ]

    def validate_next_task(self, next_task):
        """
        Ensures next_task matches contract
        """

        if not isinstance(next_task, dict):
            raise TypeError("next_task must be dict")

        for field in self.REQUIRED_FIELDS:
            if field not in next_task:
                raise ValueError(
                    f"Missing field in next_task: {field}"
                )

        return True