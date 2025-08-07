from typing import Generic, List, Optional, TypeVar
from src.repository.base import BaseRepository

ModelType = TypeVar("ModelType")
RepositoryType = TypeVar("RepositoryType")

class BaseService(Generic[ModelType]):
    
    def __init__(self, repository: BaseRepository[ModelType]):
        self.repository = repository
        
    def get(self, id: int) -> Optional[ModelType]:
        return self.repository.get(id)

    def get_all(self) -> List[ModelType]:
        return self.repository.get_all()

    def create(self, obj_in: dict) -> ModelType:
        return self.repository.create(obj_in)

    def update(self, id: int, obj_in: dict) -> Optional[ModelType]:
        db_obj = self.repository.get(id)
        if not db_obj:
            return None
        return self.repository.update(db_obj, obj_in)

    def delete(self, id: int) -> None:
        return self.repository.delete(id)
        