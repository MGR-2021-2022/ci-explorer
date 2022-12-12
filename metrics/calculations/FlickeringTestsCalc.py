from metrics.calculations.Calc import Calc
from metrics.results.FlickeringTestsResult import FlickeringTestsResult
from model.Repository import Repository


class FlickeringTestsCalc(Calc):
    def execute(repo: Repository) -> FlickeringTestsResult:
        result = FlickeringTestsResult()
        inspected_checks = []
        for pull in repo.pull_requests:
            previous_commit_failed = False
            for commit in pull.commits:
                if commit.has_checks_in(inspected_checks):
                    continue
                commit.add_check_to(inspected_checks)
                current_commit_failed = False
                if commit.check_runs is not None and len(commit.check_runs) > 0:
                    result.increment_pushes()
                    for check in commit.check_runs:
                        if check.has_problem():
                            current_commit_failed = True
                            break
                    if previous_commit_failed and not current_commit_failed and commit.modified_lines == 0:
                        result.increment_flickering_tests()
                    previous_commit_failed = current_commit_failed
        return result
