from metrics.calculations.Calc import Calc
from metrics.results.ReactionTimeResult import ReactionTimeResult
from metrics.results.Result import Result
from metrics.results.SuccessFailResult import SuccessFailResult
from model.Repository import Repository


# 6


class ReactionTimeCalc(Calc):
    def execute(repo: Repository) -> Result:
        result = SuccessFailResult(ReactionTimeResult)

        for pull in repo.pull_requests:
            previous_commit_failed = False
            previous_commit_date = None
            for commit in pull.commits:
                current_commit_failed = False
                current_commit_date = commit.created_at
                if commit.has_checks():
                    for check in commit.check_runs:
                        if check.is_failed():
                            current_commit_failed = True
                            break

                    if previous_commit_date is not None:
                        sub_result: ReactionTimeResult = result.getFail() if previous_commit_failed else result.getSuccess()
                        sub_result.increment_pushes()
                        sub_result.add_to_reaction_time((current_commit_date - previous_commit_date).seconds / 3600)
                    previous_commit_date = current_commit_date
                    previous_commit_failed = current_commit_failed

        return result
