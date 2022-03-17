from SqlAlchemyBase import Session
from model.PullRequest import PullRequest
from model.Repository import Repository


#6

# reaction time in seconds
def count_when_inspection_was_not_enough(repo: Repository) -> object:
    result = [0] * 9999

    for pull in repo.pull_requests:
        previous_commit_passed = False
        passed_commits = 0
        for commit in pull.commits:
            current_commit_passed = True
            current_commit_date = commit.created_at
            if commit.check_runs is not None and len(commit.check_runs) > 0:
                for check in commit.check_runs:
                    if(check.conclusion == 'failure'):
                        current_commit_passed = False
                        break

                if previous_commit_passed is True:
                    passed_commits += 1
                    result[passed_commits] += 1

                previous_commit_passed = current_commit_passed

    return result


db_session = Session()
# db_manager = DbManager(db_session) # todo część wspólna z mainem

repos = db_session.query(Repository).all()

for repo in repos:
    print(repo.name)
    result = count_when_inspection_was_not_enough(repo)
    print(result)
    print(sum(result))

# fajnie by było sprawdzić rekurencyjnie, i czy potem psuje sie
# czy napewno same faile udowadniają, że był sukces
# dodać procentowo, ile wgl pushy z daną liczbą sukcesów istnieje
