from typing import TypedDict

from metrics.calculations.FailedTests.Condition import Condition
from metrics.calculations.FailedTests.conditions.InspectionTimeCondition import InspectionTimeCondition


class Group:
    def __init__(self, label: str, condition: Condition):
        self.label = label
        self.condition = condition

class GroupsFactory:
    def getInspectionTimeGroups(self):
        return [
            Group("0-10", InspectionTimeCondition(0, 10)),
            Group("10-20", InspectionTimeCondition(10, 20)),
            Group("20-30", InspectionTimeCondition(20, 30)),
            Group("30-40", InspectionTimeCondition(30, 40)),
            Group("50-60", InspectionTimeCondition(50, 60)),
            Group("60-90", InspectionTimeCondition(60, 90)),
            Group("90-999999", InspectionTimeCondition(90, 999999))
        ]
