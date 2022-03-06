from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from SqlAlchemyBase import Base
from model.Repository import Repository


class PullRequest(Base):
    __tablename__ = "pull_request"

    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    repository_id = Column(Integer, ForeignKey('repository.id'))
    repository = relationship(Repository.__name__, back_populates="pull_requests")
    status = Column(String)
    created_at = Column(DateTime)
    commits = relationship("Commit", back_populates="pull_request")
