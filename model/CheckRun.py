from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from SqlAlchemyBase import Base


class CheckRun(Base):
    __tablename__ = "check_run"

    id = Column(Integer, primary_key=True)
    github_id = Column(Integer)
    name = Column(String)
    check_suit_id = Column(String)
    status = Column(String)
    conclusion = Column(String)
    order_number = Column(Integer)
    total_count = Column(Integer)
    commit_id = Column(Integer, ForeignKey('commit.id'))
    commit = relationship("Commit", back_populates="check_runs")
    started_at = Column(DateTime)
    finished_at = Column(DateTime)

    def is_failed(self) -> bool:
        return self.conclusion == "failure" or self.conclusion == "cancelled" or self.conclusion is None

    def is_success(self) -> bool:
        return not self.is_failed()