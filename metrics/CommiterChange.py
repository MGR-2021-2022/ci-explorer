from SqlAlchemyBase import Session
from model.PullRequest import PullRequest
from model.Repository import Repository


#7


def count_number_of_commits(repo: Repository) -> object:
    result = {
        "success": {"pull_count": 0, "authors_count": 0, "first_and_last": 0, "always": 0},
        "fail": {"pull_count": 0, "authors_count": 0, "first_and_last": 0, "always": 0}
    }

    pull_with_success_count = {"pull_count": 0, "commit_count": 0}

    for pull in repo.pull_requests:
        fail_in_pr = False
        authors = []
        first_author = None
        last_author = None
        same_author = True
        for commit in pull.commits:
            author = commit.author.name
            if first_author is None:
                first_author = author
            elif first_author != author:
                same_author = False
            last_author = author
            if author not in authors:
                authors.append(author)
            for check in commit.check_runs:
                if (check.conclusion == 'failure'):
                    fail_in_pr = True
                    break
        label = "fail" if fail_in_pr else "success"
        result[label]["pull_count"] += 1
        result[label]["authors_count"] += len(authors)
        result[label]["first_and_last"] += first_author == last_author
        result[label]["always"] += same_author


    return result


def print_result(label: str, result: object) -> None:
    print(label + "-> pulls: " + str(result[label]["pull_count"]) + " | authors: " + str(result[label]["authors_count"])
          + " (average: " + str(result[label]["authors_count"]/result[label]["pull_count"]) +")| first and last same: "
          + str(result[label]["first_and_last"]) + " (average: "
          + str(result[label]["first_and_last"]/result[label]["pull_count"]) + ")| always same author: "
          + str(result[label]["always"]) + " (average: " + str(result[label]["always"]/result[label]["pull_count"]) + ")")

db_session = Session()
# db_manager = DbManager(db_session) # todo część wspólna z mainem

repos = db_session.query(Repository).all()

for repo in repos:
    print(repo.name)
    result = count_number_of_commits(repo)
    print_result("fail", result)
    print_result("success", result)


# jak duze byly te commity, bo pewnie roznica bierze sie z tego ze successy to byly pushe pierdolek