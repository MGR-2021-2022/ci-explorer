from metrics.calculations.FailedTests.Condition import Condition
from metrics.calculations.FailedTests.Measure import Measure
from model.CheckRun import CheckRun
from model.Commit import Commit
from model.PullRequest import PullRequest


class ListCondition(Condition):
    def __init__(self, measure: Measure, value_list: list):
        self.measure = measure
        self.list = value_list

    def is_fulfilled(self, pull: PullRequest, commit: Commit = None, check: CheckRun = None) -> bool:
        value = self.measure.value(pull, commit, check)
        if value in self.list:
            return True
        return False
