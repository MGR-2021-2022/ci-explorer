from typing import List, Dict

from metrics.results.FailedTests.SingleResult import SingleResult
from metrics.results.Result import Result


class GroupResult(Result):
    def __init__(self):
        self.results: Dict[str, SingleResult] = {}

    def getResult(self, label: str) -> SingleResult:
        return self.results[label]

    def setResult(self, label: str, result: SingleResult):
        self.results[label] = result

    def print(self):
        for label in self.results.keys():
            print(label)
            self.results[label].print()
