import re

from metrics.calculations.Calc import Calc
from metrics.calculations.FailedTests.measures.CodeLinesChangedHelper import CodeLinesChangedHelper
from metrics.results.FilesChangedAfterFailResult import FilesChangedAfterFailResult
from model.Repository import Repository


class FilesChangedAfterFailCalc(Calc):
    def execute(repo: Repository) -> FilesChangedAfterFailResult:
        result = FilesChangedAfterFailResult()
        for pull in repo.pull_requests:
            previous_commit_failed = False
            for commit in pull.commits:
                current_commit_failed = False
                if commit.has_checks():
                    for check in commit.check_runs:
                        if check.is_failed():
                            current_commit_failed = True
                            result.increment_fails()
                            break
                    if previous_commit_failed and commit.modified_lines != 0:
                        modified_src = modified_test = modified_config = False
                        for file in commit.modified_files.keys():
                            if CodeLinesChangedHelper.isSrc(file):
                                modified_src = True
                            if CodeLinesChangedHelper.isSrc(file, True):
                                modified_test = True
                            extension = re.search("(\w)+$", file).group()
                            if extension == "json" or extension == "yml" or extension == "xml":
                                modified_config = True

                        result.add_to_files(modified_src, modified_test, modified_config)
                    previous_commit_failed = current_commit_failed
        return result

#porownac z normalnymi wynikami edycji plikow