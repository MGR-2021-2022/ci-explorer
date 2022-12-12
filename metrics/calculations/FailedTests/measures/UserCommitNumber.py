from DbManager import DbManager
from SqlAlchemyBase import Session
from metrics.calculations.FailedTests.Measure import Measure
from model.Commit import Commit
from model.PullRequest import PullRequest
from model.Repository import Repository
from model.User import User


class UserCommitNumber(Measure):
    def value(self, pull: PullRequest, commit: Commit = None):
        return commit.user_commit_number

    def mark_user_commit_number(self):
        db_session = Session()
        db_manager = DbManager(db_session)
        users = db_session.query(User).all()
        repos = db_session.query(Repository).all()
        for user in users:
            if user.id < 17695:
                continue
            repo_commits = [[]] * 14
            for commit in user.commits:
                repo_commits[commit.pull_request.repository_id - 1].append(commit)
            for i in range(0, len(repos)):
                repo_commits[i].sort(key=self.sortFunc)
                for j in range (0, len(repo_commits[i])):
                    commit = repo_commits[i][j]
                    commit.user_commit_number = j + 1
                    db_manager.save(commit)
            print(user.id)

    def sortFunc(self, commit: Commit):
        return commit.created_at


# ucn = UserCommitNumber()
# ucn.mark_user_commit_number()