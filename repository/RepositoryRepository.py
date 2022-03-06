from DbManager import DbManager
from model.Repository import Repository


class RepositoryRepository:
    def __init__(self, db_manager: DbManager):
        self.db_manager = db_manager

    def findOrCreate(self, name, owner_id) -> Repository:
        repository = self.db_manager.query(Repository).filter_by(name=name).first()
        if repository is None:
            repository = Repository(name=name, owner_id=owner_id)
            self.db_manager.save(repository)
        return repository
