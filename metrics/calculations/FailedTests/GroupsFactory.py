from typing import TypedDict

from metrics.calculations.FailedTests.Condition import Condition
from metrics.calculations.FailedTests.conditions.EqualCondition import EqualCondition
from metrics.calculations.FailedTests.conditions.ListCondition import ListCondition
from metrics.calculations.FailedTests.conditions.RangeCondition import RangeCondition
from metrics.calculations.FailedTests.measures.InspectionTime import InspectionTime
from metrics.calculations.FailedTests.measures.InspectionType import InspectionType
from metrics.calculations.FailedTests.measures.IsAuthor import IsAuthor
from metrics.calculations.FailedTests.measures.SourceCodeLinesChanged import SourceCodeLinesChanged
from metrics.calculations.FailedTests.measures.Technology import Technology
from metrics.calculations.FailedTests.measures.TestCodeLinesChanged import TestCodeLinesChanged
from metrics.calculations.FailedTests.measures.UserCommitNumber import UserCommitNumber


class Group:
    def __init__(self, label: str, condition: Condition):
        self.label = label
        self.condition = condition

class GroupsFactory:

    def getInspectionTypeGroups(self):
        measure = InspectionType()
        return [
            Group("richnav", ListCondition(measure, ["richnav"])),
            Group("darwin", ListCondition(measure, ["darwin"]))
        ]

    def getInspectionTimeGroups(self):
        measure = InspectionTime()
        return [
            Group("0-10", RangeCondition(measure, 0, 10)),
            Group("10-20", RangeCondition(measure, 10, 20)),
            Group("20-30", RangeCondition(measure, 20, 30)),
            Group("30-40", RangeCondition(measure, 30, 40)),
            Group("50-60", RangeCondition(measure, 50, 60)),
            Group("60-90", RangeCondition(measure, 60, 90)),
            Group("90-999999", RangeCondition(measure, 90, 999999))
        ]

    def getIsAuthorGroups(self):
        measure = IsAuthor()
        return [
            Group("Author", EqualCondition(measure, True)),
            Group("Not author", EqualCondition(measure, False))
        ]

    def getUserCommitNumberGroups(self):
        measure = UserCommitNumber()
        return [
            Group("0-200", RangeCondition(measure, 0, 100)),
            Group("100-300", RangeCondition(measure, 100, 300)),
            Group("300-500", RangeCondition(measure, 300, 500)),
            Group("500-700", RangeCondition(measure, 500, 700)),
            Group("700-1200", RangeCondition(measure, 700, 1200)),
            Group("1200-2000", RangeCondition(measure, 1200, 2000)),
            Group("2000-999999", RangeCondition(measure, 2000, 999999))
        ]

    def getTechnologyGroups(self):
        measure = Technology()
        return [
            Group("TypeScript", EqualCondition(measure, "TypeScript")),
        ]

    def getSourceCodeLinesChanged(self):
        measure = SourceCodeLinesChanged()
        return [
            Group("0-10", RangeCondition(measure, 0, 10)),
            Group("10-30", RangeCondition(measure, 10, 30)),
            Group("30-50", RangeCondition(measure, 30, 50)),
            Group("50-100", RangeCondition(measure, 50, 100)),
            Group("100-200", RangeCondition(measure, 100, 200)),
            Group("200-500", RangeCondition(measure, 200, 500)),
            Group("500-2000", RangeCondition(measure, 500, 2000)),
            Group("2000-5000", RangeCondition(measure, 2000, 5000)),
            Group("5000-999999", RangeCondition(measure, 5000, 99999))
        ]

    def getTestCodeLinesChanged(self):
        measure = TestCodeLinesChanged()
        return [
            Group("0-10", RangeCondition(measure, 0, 10)),
            Group("10-30", RangeCondition(measure, 10, 30)),
            Group("30-50", RangeCondition(measure, 30, 50)),
            Group("50-100", RangeCondition(measure, 50, 100)),
            Group("100-200", RangeCondition(measure, 100, 200)),
            Group("200-500", RangeCondition(measure, 200, 500)),
            Group("500-2000", RangeCondition(measure, 500, 2000)),
            Group("2000-5000", RangeCondition(measure, 2000, 5000)),
            Group("5000-999999", RangeCondition(measure, 5000, 99999))
        ]