from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from SqlAlchemyBase import Base
from model.CheckRun import CheckRun


class Commit(Base):
    __tablename__ = "commit"

    id = Column(Integer, primary_key=True)
    hash = Column(String)
    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship("User", back_populates="commits")
    modified_lines = Column(Integer)
    modified_files = Column(JSON)
    order_number = Column(Integer)
    pull_request_id = Column(Integer, ForeignKey('pull_request.id'))
    pull_request = relationship("PullRequest", back_populates="commits")
    created_at = Column(DateTime)
    check_runs = relationship(CheckRun.__name__, back_populates="commit")
    user_commit_number = Column(Integer)

    def has_checks(self) -> bool:
        return self.check_runs is not None and len(self.check_runs) > 0

    def has_failed_inspection(self) -> bool:
        for check_run in self.check_runs:
            if check_run.is_failed():
                return True
        return False

    def get_inspection_start(self) -> datetime:
        earliest_start = None

        for check_run in self.check_runs:
            if check_run.started_at is not None and earliest_start is None:
                earliest_start = check_run.started_at
            elif earliest_start > check_run.started_at:
                earliest_start = check_run.started_at

        return earliest_start

    def get_inspection_end(self) -> datetime:
        latest_end = None

        for check_run in self.check_runs:
            if check_run.finished_at is not None and latest_end is None:
                latest_end = check_run.finished_at
            elif check_run.finished_at is not None and latest_end < check_run.finished_at:
                latest_end = check_run.finished_at

        return latest_end
