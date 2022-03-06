import csv

from DbManager import DbManager
from SqlAlchemyBase import Session
from model.PullRequest import PullRequest

header = ['lines_edited', 'is_after_check_fail', 'files_edited', 'inspection_passed']
data_rows = []



with open('commit_after_failure.csv', 'w', encoding='UTF8') as f:
    db_session = Session()
    db_manager = DbManager(db_session)

    pull_requests = db_manager.query(PullRequest).all()

    for pull_request in pull_requests:
        is_after_check_fail = False
        for commit in pull_request.commits:
            check_runs_fail = any(inspection.conclusion == 'failure' or inspection.conclusion == 'cancelled' for inspection in commit.check_runs)
            commit_row = [commit.modified_lines, is_after_check_fail, commit.modified_files, not check_runs_fail]
            is_after_check_fail = check_runs_fail

            data_rows.append(commit_row)

    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    for data_row in data_rows:
        writer.writerow(data_row)