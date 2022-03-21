from SqlAlchemyBase import Session
from model.PullRequest import PullRequest
from model.Repository import Repository


#3


def count_lines_written(repo: Repository) -> object:
    result = {
        "lines_fail": 0,
        "lines_next": 0,
        "lines_in_pr": 0,
        "comparison_to_previous": 0,
        "commit_comp_count": 0,
        "comparison_to_pr": 0,
        "pr_comp_count": 0
    }

    pull_with_success_count = {"pull_count": 0, "commit_count": 0}

    for pull in repo.pull_requests:
        prev_fail = False
        total_lines = 0
        prev_lines = 0
        next_lines = []
        for commit in pull.commits:
            curr_fail = False
            curr_lines = commit.modified_lines
            for check in commit.check_runs:
                if (check.conclusion == 'failure'):
                    curr_fail = True
                    break

            if prev_fail and prev_lines != 0:
                result["lines_fail"] += prev_lines
                result["lines_next"] += curr_lines
                result["comparison_to_previous"] += curr_lines / prev_lines
                result["commit_comp_count"] += 1
                next_lines.append(curr_lines)

            total_lines += curr_lines
            prev_lines = curr_lines
            prev_fail = curr_fail

        result["lines_in_pr"] += total_lines

        for after_fail_lines in next_lines:
            result["comparison_to_previous"] += after_fail_lines / total_lines
            result["commit_comp_count"] += 1

    print(result)

    return result


db_session = Session()
# db_manager = DbManager(db_session) # todo część wspólna z mainem

repos = db_session.query(Repository).all()

for repo in repos:
    print(repo.name)
    result = count_lines_written(repo)
    # print_result("fail", result)
    # print_result("success", result)


#naiwne podejście, sprawdzamy pierwszy commit po failu
#policzyc ile lini