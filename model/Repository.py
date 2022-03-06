from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from SqlAlchemyBase import Base
from model.User import User


class Repository(Base):
    __tablename__ = "repository"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    pull_requests = relationship("PullRequest", back_populates="repository")
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship(User.__name__, back_populates="repositories")
    # created_at = Column(DateTime)
    language = Column(String)
    labels = Column(JSON)
