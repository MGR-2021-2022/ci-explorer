from datetime import datetime
from typing import Dict

from metrics.results.PipelineGrowthResult.MonthResult import MonthResult
from metrics.results.Result import Result


class PipelineGrowthResult(Result):
    def __init__(self):
        self.results: Dict[str, MonthResult] = {}

    def __add__(self, o):
        results = {}
        # for label in self.results.keys():
        #     results[label] = self.results[label] + o.results[label]
        group_result = PipelineGrowthResult()
        group_result.results = results
        return group_result

    def addMinutes(self, creation_date: datetime, minutes: int):
        label = str(creation_date.month) + "-" + str(creation_date.year)
        if label not in self.results:
            self.results[label] = MonthResult(creation_date)
        self.results[label].add_minutes(minutes)


    def print(self):
        for label in self.results.keys():
            print(label)
            self.results[label].print()