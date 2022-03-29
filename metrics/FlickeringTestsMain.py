from SqlAlchemyBase import Session
from metrics.helpers.ResultsHelper import ResultsHelper
from metrics.helpers.StatusRecognizer import StatusRecognizer
from metrics.results.FlickeringTestsResult import FlickeringTestsResult
from model.PullRequest import PullRequest
from model.Repository import Repository


#8


def count_flickering_tests(repo: Repository) -> FlickeringTestsResult:
    result = FlickeringTestsResult()
    for pull in repo.pull_requests:
        previous_commit_failed = False
        for commit in pull.commits:
            current_commit_failed = False
            if commit.check_runs is not None and len(commit.check_runs) > 0:
                result.increment_pushes()
                for check in commit.check_runs:
                    if StatusRecognizer.is_failed(check):
                        current_commit_failed = True
                        break
                if previous_commit_failed and not current_commit_failed and commit.modified_lines == 0:
                    result.increment_flickering_tests()
                previous_commit_failed = current_commit_failed
    return result


db_session = Session()
# db_manager = DbManager(db_session) # todo część wspólna z mainem

repos = db_session.query(Repository).all()

total_result = FlickeringTestsResult()

for repo in repos:
    result = count_flickering_tests(repo)
    print(repo.name)
    result.print()
    total_result = total_result + result

print("In total:")
total_result.print()
# 0 flickering tsts for now