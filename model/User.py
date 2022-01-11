from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from SqlAlchemyBase import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    commits = relationship("Commit", back_populates="author")


