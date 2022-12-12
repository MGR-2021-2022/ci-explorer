from typing import List, Dict

from metrics.results.FailedTests.SingleResult import SingleResult
from metrics.results.Result import Result


class GroupResult(Result):
    def __init__(self):
        self.results: Dict[str, SingleResult] = {}

    def __add__(self, o):
        results = {}
        for label in self.results.keys():
            results[label] = self.results[label] + o.results[label]
        group_result = GroupResult()
        group_result.results = results
        return group_result

    def getResult(self, label: str) -> SingleResult:
        return self.results[label]

    def setResult(self, label: str, result: SingleResult):
        self.results[label] = result

    def print(self):
        results = SingleResult()
        for label in self.results.keys():
            # print(label)
            self.results[label].print()
            results += self.results[label]
            # print("")
        # print("Total")
        results.print()
