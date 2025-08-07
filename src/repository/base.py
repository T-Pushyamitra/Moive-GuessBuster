from typing import TypeVar, Generic, Type
from src.core.settings import Session

ModelType = TypeVar("ModelType")

class BaseRepository(Generic[ModelType]):
    
    def __init__(self, db: Session, model: Type[ModelType]):
        self.db = db
        self.model = model
        
    def get(self, id):
        return self.db.query(self.model).get(id)
    
    def get_all(self, limit, offset):
        return self.db.query(self.model).offset(offset).limit(limit).all()
    
    def create(self, obj_in: dict) -> ModelType:
        db_obj = self.model(**obj_in)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update(self, db_obj: ModelType, obj_in: dict) -> ModelType:
        for field, value in obj_in.items():
            setattr(db_obj, field, value)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, id: int) -> None:
        obj = self.get(id)
        if obj:
            self.db.delete(obj)
            self.db.commit()