from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Type, Union, List
from src.core.settings import Session

ModelType = TypeVar("ModelType")

class BaseRepository(ABC, Generic[ModelType]):
    """Base class for Repositiory

    Args:
        ABC (_type_): 
        Generic (_type_): 
    """
    
    def __init__(self, db: Session, model: Type[ModelType]):
        self.db = db
        self.model = model
    
    def __getattr__(self, name: str) -> Union[Type[ModelType], List[Type[ModelType]]]:
        """_summary_

        Args:
            name (str): Column name of the model
            first (bool, optional): Make it true if we want to return exactly one record. Defaults to True.

        Raises:
            AttributeError: Raise the exception for typo checking of column names of model

        Returns:
            Union[Type[ModelType], List[Type[ModelType]]]: Returns the list of filtered records
        """
        if name.startswith("get_by__"):
            field = name[len("get_by__"):]

            def getter(value, first=True):
                if not hasattr(self.model, field):
                    raise AttributeError(f"'{self.model.__name__}' has no attribute '{field}'")
                if first:
                    return self.db.query(self.model).filter(getattr(self.model, field)==value).first()             
                return self.db.query(self.model).filter(getattr(self.model, field)==value)           
            return getter
        raise AttributeError(f"'{type(self).__name__}' has no attribute '{name}'")
    
    @abstractmethod
    def get(self, id: int):
        pass
    
    @abstractmethod
    def get_all(self, limit: int, offset: int):
        pass
    
    @abstractmethod
    def create(self, obj_in: dict) -> ModelType:
        pass
    
    @abstractmethod
    def update(self, db_obj: ModelType, obj_in: dict) -> ModelType:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass