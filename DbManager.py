from SqlAlchemyBase import Session
from SqlAlchemyBase import Base as Model


class DbManager():
    def __init__(self, session: Session):
        self.session = session

    def save_to_db(self, model: Model):
        self.session.add(model)
        self.session.commit()

    def query(self, class_type: type):
        return self.session.query(class_type)
