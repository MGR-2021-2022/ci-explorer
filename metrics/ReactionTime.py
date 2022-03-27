from SqlAlchemyBase import Session
from metrics.helpers.ResultsHelper import ResultsHelper
from model.PullRequest import PullRequest
from model.Repository import Repository


#6

# reaction time in seconds
def measure_reaction_time(repo: Repository) -> object:
    result = {
        "success": {"reaction_time": 0, "commit_count": 0},
        "fail": {"reaction_time": 0, "commit_count": 0},
        "total": {"reaction_time": 0, "commit_count": 0}
    }

    pull_with_success_count = {"pull_count": 0, "commit_count": 0}

    for pull in repo.pull_requests:
        previous_commit_failed = False
        previous_commit_date = None
        for commit in pull.commits:
            current_commit_failed = False
            current_commit_date = commit.created_at
            if commit.check_runs is not None and len(commit.check_runs) > 0:
                for check in commit.check_runs:
                    if(check.conclusion == 'failure'):
                        current_commit_failed = True
                        break

                if previous_commit_date is not None:
                    label = "fail" if previous_commit_failed else "success"
                    result[label]["reaction_time"] += (current_commit_date - previous_commit_date).seconds/3600
                    result[label]["commit_count"] += 1
                    result["total"]["reaction_time"] += (current_commit_date - previous_commit_date).seconds / 3600
                    result["total"]["commit_count"] += 1
                previous_commit_date = current_commit_date
                previous_commit_failed = current_commit_failed

    return result


def print_result(label: str, result: object) -> None:
    print(label + "-> hours: " + str(result[label]["reaction_time"]) + " | commits: " + str(result[label]["commit_count"]) + " | average: " + str(result[label]["reaction_time"]/result[label]["commit_count"]))


db_session = Session()
# db_manager = DbManager(db_session) # todo część wspólna z mainem

repos = db_session.query(Repository).all()
total_results = {
        "success": {"reaction_time": 0, "commit_count": 0},
        "fail": {"reaction_time": 0, "commit_count": 0},
        "total": {"reaction_time": 0, "commit_count": 0}
    }
for repo in repos:
    print(repo.name)
    result = measure_reaction_time(repo)
    print_result("success", result)
    print_result("fail", result)
    print_result("total", result)
    print("")
    total_results = ResultsHelper.add_results_nested(total_results, result)

print("In total:")
print_result("success", total_results)
print_result("fail", total_results)
print_result("total", total_results)