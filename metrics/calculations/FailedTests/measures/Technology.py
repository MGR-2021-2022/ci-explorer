from metrics.calculations.FailedTests.Measure import Measure
from model.Commit import Commit
from model.PullRequest import PullRequest


class Technology(Measure):
    def value(self, pull: PullRequest, commit: Commit = None):
        return pull.repository.language
