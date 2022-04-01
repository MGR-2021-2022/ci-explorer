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

