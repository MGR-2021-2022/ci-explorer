from DbManager import DbManager
from model.User import User


class UserRepository:
    def __init__(self, db_manager: DbManager):
        self.db_manager = db_manager

    def findOrCreate(self, name) -> User:
        user = self.db_manager.query(User).filter_by(name=name).first()
        if user is None:
            user = User(name=name)
            self.db_manager.save_to_db(user)
        return user
