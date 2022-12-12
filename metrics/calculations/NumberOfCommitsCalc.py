from metrics.calculations.Calc import Calc
from metrics.results.NumberOfCommitsResult import NumberOfCommitsResult
from metrics.results.Result import Result
from metrics.results.SuccessFailResult import SuccessFailResult
from model.Repository import Repository


#4


class NumberOfCommitsCalc(Calc):
    def execute(repo: Repository) -> Result:
        result = SuccessFailResult(NumberOfCommitsResult)

        pull_numbers = []
        for pull in repo.pull_requests:
            if pull.number in pull_numbers:
                continue
            if not pull.merged:
                continue
            pull_numbers.append(pull.number)
            fail_in_pr = False
            has_checks = False
            for commit in pull.commits:
                if commit.has_checks():
                    has_checks = True
                for check in commit.check_runs:
                    if check.has_problem():
                        fail_in_pr = True
                        break
            if not has_checks:
                continue
            sub_result: NumberOfCommitsResult = result.getFail() if fail_in_pr else result.getSuccess()
            sub_result.increment_pr_count()
            sub_result.add_to_commit_count(len(pull.commits))

        return result