from typing import Type

from SqlAlchemyBase import Session
from metrics.helpers.ResultsHelper import ResultsHelper
from metrics.helpers.StatusRecognizer import StatusRecognizer
from metrics.results import CommitterChangeResult
from metrics.results.Result import Result
from metrics.results.SuccessFailResult import SuccessFailResult
from model.PullRequest import PullRequest
from model.Repository import Repository


#7


def count_number_of_commits(repo: Repository) -> CommitterChangeResult:
    result = SuccessFailResult(Type[CommitterChangeResult])

    for pull in repo.pull_requests:
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
                if StatusRecognizer.is_failed(check):
                    fail_in_pr = True
                    break
        if not has_commits:
            continue
        sub_result: CommitterChangeResult = result.getFail() if fail_in_pr else result.getSuccess()
        # 'sub_result' is CommitterChangeResult
        sub_result.increment_pr_count()
        sub_result.add_to_authors_count(len(authors))
        sub_result.add_to_first_and_last(first_author == last_author)
        sub_result.add_to_always(same_author)

        # result["total"]["pull_count"] += 1
        # result["total"]["authors_count"] += len(authors)
        # result["total"]["first_and_last"] += first_author == last_author
        # result["total"]["always"] += same_author


    return result


def print_result(label: str, result: object) -> None:
    result.print()
# db_session = Session()
# # db_manager = DbManager(db_session) # todo część wspólna z mainem
#
# repos = db_session.query(Repository).all()
#
# total_results = {
#     "success": {"pull_count": 0, "authors_count": 0, "first_and_last": 0, "always": 0},
#     "fail": {"pull_count": 0, "authors_count": 0, "first_and_last": 0, "always": 0},
#     "total": {"pull_count": 0, "authors_count": 0, "first_and_last": 0, "always": 0}
# }
# for repo in repos:
#     print(repo.name)
#     result = count_number_of_commits(repo)
#     print_result("success", result)
#     print_result("fail", result)
#     print_result("total", result)
#     print("")
#     total_results = ResultsHelper.add_results_nested(total_results, result)
#
# print("In total:")
# print_result("success", total_results)
# print_result("fail", total_results)
# print_result("total", total_results)

# jak duze byly te commity, bo pewnie roznica bierze sie z tego ze successy to byly pushe pierdolek

# wyrzucić te bez testów