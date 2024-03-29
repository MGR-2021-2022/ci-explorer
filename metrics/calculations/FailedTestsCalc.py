from typing import List

from metrics.calculations.Calc import Calc
from metrics.calculations.FailedTests.GroupsFactory import Group
from metrics.results.FailedTests.GroupResult import GroupResult
from metrics.results.FailedTests.SingleResult import SingleResult
from model.Repository import Repository

#1
class FailedTestsCalc(Calc):
    def execute(repo: Repository, groups: List[Group]) -> GroupResult:
        results = GroupResult()
        inspected_checks = []
        for group in groups:
            results.setResult(group.label, SingleResult())
        pull_numbers = []
        for pull in repo.pull_requests:
            if pull.number in pull_numbers:
                continue
            pull_numbers.append(pull.number)
            # if not pull.merged:
            #     continue
            for commit in pull.commits:
                is_failed = False
                if commit.has_checks_in(inspected_checks):
                    continue
                commit.add_check_to(inspected_checks)
                if commit.check_runs is None or len(commit.check_runs) == 0:
                    continue
                for check in commit.check_runs:
                    if check.has_problem():
                        is_failed = True
                        break

                for group in groups:
                    if group.condition.is_fulfilled(pull, commit):
                        if is_failed:
                            results.getResult(group.label).increment_fails()
                        else:
                            results.getResult(group.label).increment_passes()

        return results


