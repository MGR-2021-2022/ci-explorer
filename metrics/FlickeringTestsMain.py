from SqlAlchemyBase import Session
from metrics.helpers.ResultsHelper import ResultsHelper
from model.PullRequest import PullRequest
from model.Repository import Repository


#8



def count_flickering_tests(repo: Repository) -> object:
    result = {"commits_with_tests": 0, "flickering_tests": 0}
    for pull in repo.pull_requests:
        previous_commit_failed = False
        for commit in pull.commits:
            current_commit_failed = False
            if commit.check_runs is not None and len(commit.check_runs) > 0:
                result["commits_with_tests"] += 1
                for check in commit.check_runs:
                    if(check.conclusion == 'failure'):
                        current_commit_failed = True
                        break
                if previous_commit_failed and not current_commit_failed and commit.modified_lines == 0:
                    result["flickering_tests"] += 1
                previous_commit_failed = current_commit_failed
    return result


def print_result(result: object):
    print(result["commits_with_tests"])
    print(result["flickering_tests"])
    print("")

db_session = Session()
# db_manager = DbManager(db_session) # todo część wspólna z mainem

repos = db_session.query(Repository).all()

total_results = {"commits_with_tests": 0, "flickering_tests": 0}

for repo in repos:
    result = count_flickering_tests(repo)
    print(repo.name)
    print_result(result)
    total_results = ResultsHelper.add_results(total_results, result)

print("In total:")
print_result(total_results)

# 0 flickering tsts for now