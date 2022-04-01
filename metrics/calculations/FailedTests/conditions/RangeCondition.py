from metrics.calculations.FailedTests.Condition import Condition
from metrics.calculations.FailedTests.measures.InspectionTime import InspectionTime
from metrics.calculations.FailedTests.measures.Measure import Measure
from model.Commit import Commit
from model.PullRequest import PullRequest


class RangeCondition(Condition):
    def __init__(self, measure: Measure, start: int, end: int):
        self.measure = measure
        self.start = start
        self.end = end

    def is_fulfilled(self, pull: PullRequest, commit: Commit = None) -> bool:
        value = self.measure.value(pull, commit)
        return self.start <= value < self.end
