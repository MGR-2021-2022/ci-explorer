from SqlAlchemyBase import Session
from model.PullRequest import PullRequest
from model.Repository import Repository


#4


def count_number_of_commits(repo: Repository) -> int:
    result = {
        "success": {"pull_count": 0, "commit_count": 0},
        "fail": {"pull_count": 0, "commit_count": 0},
        "total": {"pull_count": 0, "commit_count": 0}
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
        result["total"]["pull_count"] += 1
        result["total"]["commit_count"] += len(pull.commits)
    return result


def print_result(label: str, result: object) -> None:
    print(label + "-> pulls: " + str(result[label]["pull_count"]) + " | commits: " + str(result[label]["commit_count"]) + " | average: " + str(result[label]["commit_count"]/result[label]["pull_count"]))


db_session = Session()
# db_manager = DbManager(db_session) # todo część wspólna z mainem

repos = db_session.query(Repository).all()
total_result = {
        "success": {"pull_count": 0, "commit_count": 0},
        "fail": {"pull_count": 0, "commit_count": 0},
        "total": {"pull_count": 0, "commit_count": 0}
    }
for repo in repos:
    print(repo.name)
    result = count_number_of_commits(repo)
    print_result("success", result)
    print_result("fail", result)
    print_result("total", result)
    for row in total_result.items():
        for key in row[1].keys():
            total_result[row[0]][key] += result[row[0]][key]


print("In total:")
print_result("success", total_result)
print_result("fail", total_result)
print_result("total", total_result)

# jak duze byly te commity, bo pewnie roznica bierze sie z tego ze successy to byly pushe pierdolek