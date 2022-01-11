from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from SqlAlchemyBase import Base


class CheckRun(Base):
    __tablename__ = "check_run"

    id = Column(Integer, primary_key=True)
    hash = Column(String)
    name = Column(String)
    status = Column(String)
    order_number = Column(Integer)
    commit_id = Column(Integer, ForeignKey('commit.id'))
    commit = relationship("Commit", back_populates="check_runs")
    created_at = Column(DateTime)
