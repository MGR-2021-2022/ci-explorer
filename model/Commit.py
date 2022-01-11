from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from SqlAlchemyBase import Base


class Commit(Base):
    __tablename__ = "commit"

    id = Column(Integer, primary_key=True)
    hash = Column(String)
    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship("User", back_populates="commits")
    modified_lines = Column(Integer)
    modified_files = Column(String)
    order_number = Column(Integer)
    pull_request_id = Column(Integer, ForeignKey('pull_request.id'))
    pull_request = relationship("PullRequest", back_populates="commits")
    created_at = Column(DateTime)
    check_runs = relationship("CheckRun", back_populates="commit")
