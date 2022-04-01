from SqlAlchemyBase import Session
from metrics.calculations.FailedTests.measures.Measure import Measure
from model.Commit import Commit
from model.PullRequest import PullRequest


class UserCommitNumber(Measure):
    def value(self, pull: PullRequest, commit: Commit = None) -> int:
        db_session = Session()
        commit_ids = db_session.query(Commit.id).filter(Commit.author_id == commit.author_id).order_by(Commit.created_at).all()
        commit_ids_for_repo = [commit_id[0] for commit_id in commit_ids if db_session.query(Commit).
            where(Commit.id == commit_id[0]).one().pull_request.repository_id == pull.repository_id]
        # commit_ids_for_repo = list(map(lambda commit: commit.id, commits_for_repo))
        position = commit_ids_for_repo.index(commit.id)

        print(position)
        return position