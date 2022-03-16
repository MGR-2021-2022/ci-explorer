from SqlAlchemyBase import Session
from model.PullRequest import PullRequest
from model.Repository import Repository


#8


def count_flickering_tests(repo: Repository) -> int:
    flickering_tests_count = 0
    commits_with_tests = 0
    for pull in repo.pull_requests:
        previous_commit_failed = False
        for commit in pull.commits:
            current_commit_failed = False
            if commit.check_runs is not None and len(commit.check_runs) > 0:
                commits_with_tests += 1
                for check in commit.check_runs:
                    if(check.conclusion == 'failure'):
                        current_commit_failed = True
                        break
                if previous_commit_failed and not current_commit_failed and commit.modified_lines == 0:
                    flickering_tests_count += 1
                previous_commit_failed = current_commit_failed
    print(commits_with_tests)
    return flickering_tests_count



db_session = Session()
# db_manager = DbManager(db_session) # todo część wspólna z mainem

repos = db_session.query(Repository).all()

for repo in repos:
    print(str(count_flickering_tests(repo)))


# 0 flickering tsts for now