from model.CheckRun import CheckRun


class StatusRecognizer:
    def is_failed(check: CheckRun) -> bool:
        return check.conclusion == "failure" or check.conclusion == "cancelled" or check.conclusion is None

    def is_success(check: CheckRun) -> bool:
        return not StatusRecognizer.is_failed(check)