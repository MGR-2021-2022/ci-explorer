from DbManager import DbManager
from model.Repository import Repository


class RepositoryRepository:
    def __init__(self, db_manager: DbManager):
        self.db_manager = db_manager

    def findOrCreate(self, name, owner_id, created_at, language, topics) -> Repository:
        repository = self.db_manager.query(Repository).filter_by(name=name).first()
        if repository is None:
            repository = Repository(name=name, owner_id=owner_id, created_at=created_at, language=language, topics=topics)
            self.db_manager.save(repository)
        return repository
