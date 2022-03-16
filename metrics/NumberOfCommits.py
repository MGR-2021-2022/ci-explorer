from SqlAlchemyBase import Session
from model.PullRequest import PullRequest
from model.Repository import Repository


#4


def count_number_of_commits(repo: Repository) -> int:
    result = {
        "success": {"pull_count": 0, "commit_count": 0},
        "fail": {"pull_count": 0, "commit_count": 0}
    }

    pull_with_success_count = {"pull_count": 0, "commit_count": 0}

    for pull in repo.pull_requests:
        fail_in_pr = False
        for commit in pull.commits:
            for check in commit.check_runs:
                if (check.conclusion == 'failure'):
                    fail_in_pr = True
                    break
        label = "fail" if fail_in_pr else "success"
        result[label]["pull_count"] += 1
        result[label]["commit_count"] += len(pull.commits)

    return result


def print_result(label: str, result: object) -> None:
    print(label + "-> pulls: " + str(result[label]["pull_count"]) + " | commits: " + str(result[label]["commit_count"]) + " | average: " + str(result[label]["commit_count"]/result[label]["pull_count"]))


db_session = Session()
# db_manager = DbManager(db_session) # todo część wspólna z mainem

repos = db_session.query(Repository).all()

for repo in repos:
    print(repo.name)
    result = count_number_of_commits(repo)
    print_result("fail", result)
    print_result("success", result)


# jak duze byly te commity, bo pewnie roznica bierze sie z tego ze successy to byly pushe pierdolek