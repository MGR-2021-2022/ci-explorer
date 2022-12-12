from typing import Type

from metrics.calculations.Calc import Calc
from metrics.results.CommitterChangeResult import CommitterChangeResult
from metrics.results.Result import Result
from metrics.results.SuccessFailResult import SuccessFailResult
from model.Repository import Repository


#7


class CommitterChangeCalc(Calc):
    def execute(repo: Repository) -> Result:
        result = SuccessFailResult(CommitterChangeResult)

        pull_numbers = []
        for pull in repo.pull_requests:
            if pull.number in pull_numbers:
                continue
            pull_numbers.append(pull.number)
            fail_in_pr = False
            authors = []
            first_author = None
            last_author = None
            same_author = True
            has_commits = False
            for commit in pull.commits:
                if commit.has_checks():
                    has_commits = True
                author = commit.author.name
                if first_author is None:
                    first_author = author
                elif first_author != author:
                    same_author = False
                last_author = author
                if author not in authors:
                    authors.append(author)
                for check in commit.check_runs:
                    if check.has_problem():
                        fail_in_pr = True
                        break
            if not has_commits:
                continue
            sub_result: CommitterChangeResult = result.getFail() if fail_in_pr else result.getSuccess()
            sub_result.increment_pr_count()
            sub_result.add_to_authors_count(len(authors))
            sub_result.add_to_first_and_last(first_author == last_author)
            sub_result.add_to_always(same_author)


        return result
