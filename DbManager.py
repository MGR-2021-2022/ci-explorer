from SqlAlchemyBase import Session
from SqlAlchemyBase import Base as Model


class DbManager():
    def __init__(self, session: Session):
        self.session = session

    def save(self, model: Model, flush: bool = True):
        self.session.add(model)
        self.flush()

    def remove(self, model: Model, flush: bool = True):
        self.session.delete(model)
        self.flush()

    def flush(self):
        self.session.commit()

    def query(self, class_type: type):
        return self.session.query(class_type)
