from metrics.calculations.FailedTests.Measure import Measure
from model.CheckRun import CheckRun
from model.Commit import Commit
from model.PullRequest import PullRequest

class InspectionType(Measure):
    def value(self, pull: PullRequest, commit: Commit = None, check: CheckRun = None):
        return check.name
