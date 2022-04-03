from metrics.calculations.FailedTests.Condition import Condition
from metrics.calculations.FailedTests.Measure import Measure
from model.Commit import Commit
from model.PullRequest import PullRequest


class EqualCondition(Condition):
    def __init__(self, measure: Measure, value):
        self.measure = measure
        self.value = value

    def is_fulfilled(self, pull: PullRequest, commit: Commit = None) -> bool:
        return self.measure.value(pull, commit) == self.value
