from metrics.calculations.FailedTests.Condition import Condition
from metrics.calculations.FailedTests.measures.InspectionTime import InspectionTime
from model.PullRequest import PullRequest


class InspectionTimeCondition(Condition):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.inspectionTime = InspectionTime()

    def isFulfilled(self, pull: PullRequest) -> bool:
        avgTime = self.inspectionTime.getAvgTime(pull)
        return self.start <= avgTime < self.end
