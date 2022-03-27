from SqlAlchemyBase import Session
from metrics.helpers.ResultsHelper import ResultsHelper
from model.PullRequest import PullRequest
from model.Repository import Repository


#6

# reaction time in seconds
def count_when_inspection_was_not_enough(repo: Repository) -> object:
    # result = [0] * 99
    result = {"pushes": 0, "passed_pushes": 0, "pr_with_pass": 0, "pr": 0, "commit_after_pass": [0] * 99}
    result["pr"] = len(repo.pull_requests)

    for pull in repo.pull_requests:
        push_with_pass = False
        previous_commit_passed = False
        passed_commits = 0
        for commit in pull.commits:
            current_commit_passed = True
            if commit.check_runs is not None and len(commit.check_runs) > 0:
                result["pushes"] += 1
                for check in commit.check_runs:
                    if(check.conclusion == 'failure'):
                        current_commit_passed = False
                        break

                if previous_commit_passed is True:
                    push_with_pass = True
                    passed_commits += 1
                    result["commit_after_pass"][passed_commits] += 1

                previous_commit_passed = current_commit_passed

        result["passed_pushes"] += passed_commits
        result["pr_with_pass"] += push_with_pass
    return result


def print_result(result):
    print(result)
    print(result["pushes"])
    print(result["passed_pushes"])
    print(result["pushes"]/result["passed_pushes"])
    print(result["pr"])
    print(result["pr_with_pass"])
    print(result["pr"]/result["pr_with_pass"])
    print("")



db_session = Session()
# db_manager = DbManager(db_session) # todo część wspólna z mainem

repos = db_session.query(Repository).all()

total_results = {"pushes": 0, "passed_pushes": 0, "pr_with_pass": 0, "pr": 0, "commit_after_pass": [0] * 99}

for repo in repos:
    print(repo.name)

    result = count_when_inspection_was_not_enough(repo)
    print_result(result)

    total_results = ResultsHelper.add_results(total_results, result)
    # print(sum(result))

print("In total:")
print_result(total_results)


# dodać procentowo, ile wgl pushy z daną liczbą sukcesów istnieje
# ile pushy