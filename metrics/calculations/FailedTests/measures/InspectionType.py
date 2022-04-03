from metrics.calculations.FailedTests.Measure import Measure
from model.Commit import Commit
from model.PullRequest import PullRequest

class InspectionType(Measure):
    def value(self, pull: PullRequest, commit: Commit = None):
        failed_check_names = []
        for check_run in commit.check_runs:
            if check_run.conclusion == "failure":
                failed_check_names.append(check_run.name)
        return failed_check_names
