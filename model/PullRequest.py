from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from SqlAlchemyBase import Base


class PullRequest(Base):
    __tablename__ = "pull_request"

    id = Column(Integer, primary_key=True)
    hash = Column(String)
    repository_id = Column(Integer, ForeignKey('repository.id'))
    repository = relationship("Repository", back_populates="pull_requests")
    status = Column(String)
    created_at = Column(DateTime)
    commits = relationship("Commit", back_populates="pull_request")
