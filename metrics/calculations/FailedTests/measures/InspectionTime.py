import datetime

from SqlAlchemyBase import Session
from metrics.helpers.StatusRecognizer import StatusRecognizer
from model.Commit import Commit
from model.PullRequest import PullRequest
from model.Repository import Repository

minutes = [0] * 10080


class InspectionTime:
    def value(self, pull: PullRequest, commit: Commit) -> int:
        pull_time = datetime.timedelta(0)
        pull_time_count = 0
        for commit in pull.commits:
            earliest_start = None
            latest_end = None

            passed = True
            for check_run in commit.check_runs:
                if StatusRecognizer.is_failed(check_run):
                    passed = False
            if passed is False:
                continue

            for check_run in commit.check_runs:
                if check_run.started_at is not None and earliest_start is None:
                    earliest_start = check_run.started_at
                elif earliest_start > check_run.started_at:
                    earliest_start = check_run.started_at
                if latest_end is None:
                    latest_end = check_run.finished_at
                elif check_run.finished_at is not None and latest_end < check_run.finished_at:
                    latest_end = check_run.finished_at
            if earliest_start is not None and latest_end is not None:
                time = latest_end - earliest_start
                pull_time += time
                pull_time_count += 1
        if pull_time_count != 0:
            avg_time = pull_time / pull_time_count
            if avg_time.seconds // 60 < 10:
                print("avg: " + str(avg_time) + " - " + str(pull.number))
            return avg_time.seconds // 60
        else:
          return -1

    def getAll(self):
        db_session = Session()
        # db_manager = DbManager(db_session) # todo część wspólna z mainem
        repos = db_session.query(Repository).all()
        for repo in repos:
            for pull in repo.pull_requests:
                if pull.merged == False:
                    continue
                avgTime = self.getAvgTime(pull)
                if avgTime != -1:
                    minutes[avgTime] += 1

# inspection = InspectionTime()
# inspection.getAll()
#
# with open('inspection_time_report.txt', 'a') as the_file:
#     for minute in minutes:
#         the_file.write(str(minute)+'\n')
# print(sum(minutes))