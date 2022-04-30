from metrics.calculations.Calc import Calc
from metrics.results.IsInspectionEnoughResult import IsInspectionEnoughResult
from metrics.results.Result import Result
from model.Repository import Repository


class IsInspectionEnoughCalc(Calc):
    def execute(repo: Repository) -> Result:
        result = IsInspectionEnoughResult()
        for pull in repo.pull_requests:
            push_with_pass = False
            previous_commit_passed = False
            has_checks = False
            passed_commits = 0
            for commit in pull.commits:
                current_commit_passed = True
                if commit.check_runs is not None and len(commit.check_runs) > 0:
                    has_checks = True
                    result.add_to_pushes(1)
                    for check in commit.check_runs:
                        if check.is_failed():
                            current_commit_passed = False
                            break

                    if previous_commit_passed is True:
                        push_with_pass = True
                        passed_commits += 1

                    previous_commit_passed = current_commit_passed
            if has_checks:
                result.add_to_pulls(1)
            result.add_to_pushes_after_pass(passed_commits)
            result.add_to_pulls_with_after_pass(push_with_pass)
        return result
