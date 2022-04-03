from metrics.calculations.FailedTests.Measure import Measure
from model.Commit import Commit
from model.PullRequest import PullRequest


class IsAuthor(Measure):
    def value(self, pull: PullRequest, commit: Commit = None):
        return commit.author_id == pull.repository.owner_id
