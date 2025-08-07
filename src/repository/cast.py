
from .base import BaseRepository
from src.models.domain.cast import Cast

class CastRepository(BaseRepository[Cast]):
    
    def __init__(self, db):
        super().__init__(db, Cast)
        
    def get_by_name(self, name: str):
        return self.db.query(self.model).get(self.model.name.lower() == name).first()
    
        