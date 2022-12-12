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
        if minutes == 0:
            return
        label = str(creation_date.month) + "-" + str(creation_date.year)
        if label not in self.results:
            self.results[label] = MonthResult(creation_date)
        self.results[label].add_minutes(minutes)


    def print(self):
        i = 1
        original_months = 0
        original_time = 0
        sorted_labels = sorted(self.results.keys(), key=lambda key: self.label_to_datetime(key))

        while original_months < 3 and original_months < len(sorted_labels):
            original_time += (self.results[sorted_labels[original_months]].minutes / self.results[sorted_labels[original_months]].pushes)
            original_months += 1
        original_time_avg = original_time/original_months
        print(self.round(original_time_avg))
        for label in sorted_labels:
            # print(label)
            self.results[label].print(i, original_time_avg)
            i+=1

    def label_to_datetime(self, label: str) -> datetime:
        return datetime.strptime(label, '%m-%Y')
