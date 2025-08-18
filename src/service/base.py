from typing import Generic, List, Optional, TypeVar
from abc import ABC
from src.repository.base import BaseRepository


ModelType = TypeVar("ModelType")
RepositoryType = TypeVar("RepositoryType")

class BaseService(ABC, Generic[ModelType]):
    """Base class for Service

    Args:
        Generic (_type_): 
    """
    
    def __init__(self, repository: BaseRepository[ModelType]):
        self.repository = repository
    
    def get(self, id: int) -> Optional[ModelType]:
        return self.repository.get(id)

    def get_all(self) -> List[ModelType]:
        return self.repository.get_all(10, 0)

    def create(self, obj_in: dict) -> ModelType:
        return self.repository.create(obj_in)

    def update(self, id: int, obj_in: dict) -> Optional[ModelType]:
        pass

    def delete(self, id: int) -> None:
        pass
        