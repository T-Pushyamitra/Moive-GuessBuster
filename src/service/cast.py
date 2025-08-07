from .base import BaseService
from src.repository.cast import CastRepository
from src.models.domain.cast import Cast
from src.core.settings import Session

class CastService(BaseService[Cast]):
    
    def __init__(self, db: Session):
        repository = CastRepository(db)
        super().__init__(repository)
        
        self.db = db
        self.repository : CastRepository = repository
        
    def get_by_name(self, name):
        return self.repository.get_by_name(name)
    
        
        