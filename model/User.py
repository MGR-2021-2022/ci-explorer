from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from SqlAlchemyBase import Base
from model.Commit import Commit


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    commits = relationship(Commit.__name__, back_populates="author")
    repositories = relationship("Repository", back_populates="owner")
