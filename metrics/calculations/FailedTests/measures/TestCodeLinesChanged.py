from metrics.calculations.FailedTests.Measure import Measure
from metrics.calculations.FailedTests.measures.CodeLinesChangedHelper import CodeLinesChangedHelper
from model.Commit import Commit
from model.PullRequest import PullRequest


class TestCodeLinesChanged(Measure):
    def value(self, pull: PullRequest, commit: Commit = None):
        lines = 0
        for filename in commit.modified_files.keys():
            if CodeLinesChangedHelper.isSrc(filename, True):
                lines += commit.modified_files[filename]
        return lines
