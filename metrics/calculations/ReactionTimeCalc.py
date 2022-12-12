from metrics.calculations.Calc import Calc
from metrics.results.ReactionTimeResult import ReactionTimeResult
from metrics.results.Result import Result
from metrics.results.SuccessFailResult import SuccessFailResult
from model.Repository import Repository


# 6


class ReactionTimeCalc(Calc):
    def execute(repo: Repository) -> Result:
        # result = SuccessFailResult(ReactionTimeResult)

        result = ReactionTimeResult()
        pull_numbers = []
        for pull in repo.pull_requests:
            if pull.number in pull_numbers:
                continue
            pull_numbers.append(pull.number)
            previous_commit_failed = False
            previous_commit_date = None
            for commit in pull.commits:
                current_commit_failed = False
                current_commit_date = commit.created_at
                if commit.has_checks():
                    for check in commit.check_runs:
                        if check.has_problem():
                            current_commit_failed = True
                            break

                    if previous_commit_date is not None and previous_commit_failed and not current_commit_failed:
                        result.add_to_reaction_time((current_commit_date - previous_commit_date).total_seconds() / 3600)

                    previous_commit_date = current_commit_date
                    previous_commit_failed = current_commit_failed

        return result
