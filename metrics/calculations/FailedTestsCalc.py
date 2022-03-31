from typing import List

from metrics.calculations.Calc import Calc
from metrics.calculations.FailedTests.GroupsFactory import Group
from metrics.helpers.ResultsHelper import ResultsHelper
from metrics.helpers.StatusRecognizer import StatusRecognizer
from metrics.results.FailedTests.GroupResult import GroupResult
from metrics.results.FailedTests.SingleResult import SingleResult
from model.Repository import Repository

#1
class FailedTestsCalc(Calc):
    def execute(repo: Repository, groups: List[Group]) -> GroupResult:
        results = GroupResult()
        for group in groups:
            results.setResult(group.label, SingleResult())
        for pull in repo.pull_requests:
            if not pull.merged:
                continue
            for commit in pull.commits:
                is_failed = False
                if commit.check_runs is None or len(commit.check_runs) == 0:
                    continue
                for check in commit.check_runs:
                    if StatusRecognizer.is_failed(check):
                        is_failed = True
                        break

                for group in groups:
                    if group.condition.isFulfilled(pull):
                        if is_failed:
                            results.getResult(group.label).increment_fails()
                        else:
                            results.getResult(group.label).increment_passes()
                        break

        return results


