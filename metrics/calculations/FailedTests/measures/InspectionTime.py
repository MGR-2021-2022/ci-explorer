import datetime

from SqlAlchemyBase import Session
from metrics.calculations.FailedTests.Measure import Measure
from metrics.helpers.StatusRecognizer import StatusRecognizer
from model.Commit import Commit
from model.PullRequest import PullRequest
from model.Repository import Repository

minutes = [0] * 10080


class InspectionTime(Measure):
    def value(self, pull: PullRequest, commit: Commit) -> int:
        pull_time = datetime.timedelta(0)
        pull_time_count = 0
        for commit in pull.commits:
            if commit.has_failed_inspection():
                continue

            earliest_start = commit.get_inspection_start()
            latest_end = commit.get_inspection_end()

            if earliest_start is not None and latest_end is not None:
                time = latest_end - earliest_start
                pull_time += time
                pull_time_count += 1
        if pull_time_count != 0:
            avg_time = pull_time / pull_time_count
            # if avg_time.seconds // 60 < 10:
            #     print("avg: " + str(avg_time) + " - " + str(pull.number))
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