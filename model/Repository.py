from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from SqlAlchemyBase import Base


class Repository(Base):
    __tablename__ = "repository"

    id = Column(Integer, primary_key=True)
    # name = Column(String)
    pull_requests = relationship("PullRequest", back_populates="repository")
    status = Column(String)
    # created_at = Column(DateTime)
