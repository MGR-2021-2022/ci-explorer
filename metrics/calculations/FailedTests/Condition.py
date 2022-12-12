from model.CheckRun import CheckRun
from model.Commit import Commit
from model.PullRequest import PullRequest


class Condition:
    def is_fulfilled(self, pull: PullRequest, commit: Commit = None, check: CheckRun = None) -> bool:
        return False
