from model.Commit import Commit
from model.PullRequest import PullRequest


class Measure:
    def value(self, pull: PullRequest, commit: Commit = None) -> int:
        return -1
