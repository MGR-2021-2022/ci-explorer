from SqlAlchemyBase import Session
from model.PullRequest import PullRequest
from model.Repository import Repository

def count_failed_tests(repo: Repository) -> int:
    failed_tests_count = 0
    commits_with_tests = 0
    for pull in repo.pull_requests:
        for commit in pull.commits:
            if commit.check_runs is not None and len(commit.check_runs) > 0:
                commits_with_tests += 1
            for check in commit.check_runs:
                if(check.conclusion == 'failure'):
                    failed_tests_count += 1
                    break
    print(commits_with_tests)
    return failed_tests_count



db_session = Session()
# db_manager = DbManager(db_session) # todo część wspólna z mainem

repos = db_session.query(Repository).all()

for repo in repos:
    print(str(count_failed_tests(repo)))


