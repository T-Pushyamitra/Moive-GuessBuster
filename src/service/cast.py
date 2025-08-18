from .base import BaseService
from src.repository.cast import CastRepository
from src.models.domain.cast import Cast
from src.core.settings import Session
from src.models.schema.cast import CastCreateSchema, CastSchema
from src.exception.custom_exception import BadRequestError
from typing import List

class CastService(BaseService[Cast]):
    
    def __init__(self, db: Session):
        repository = CastRepository(db)
        super().__init__(repository)
        
        self.db = db
        self.repository : CastRepository = repository
    
    def get_by_id(self, id: int) -> Cast:
        """Get the cast by Id

        Args:
            id (int): Id of the actor/cast

        Returns:
            Cast: 
        """
        return self.repository.get_by__id(id)
    
    def get_by_name(self, name: str) -> Cast:
        """Get the Cast by Name

        Args:
            name (str): Name of the actor/cast

        Returns:
            Cast
        """
        return self.repository.get_by__name(name)
    
    def get_by_title(self, title: str) -> List[Cast]:
        """Get the List of cast by their title

        Args:
            title (str): 

        Returns:
            List[Cast]: 
        """
        return self.repository.get_by__title(title, first=False)
        
    def create(self, casts: List[CastSchema]) -> List[Cast]:
        """Create new casts

        Args:
            casts (List[CastSchema]): 

        Returns:
            List[Cast]: 
        """
        _casts : list = [] 
        for cast in casts:
            _casts.append(self.__save(cast=cast))
        return _casts
        
    def __save(self, cast: CastCreateSchema) -> Cast:
        """Save the cast

        Args:
            cast (CastCreateSchema): 

        Returns:
            Cast: 
        """
        return self.repository.create(cast)
   
    def update(self, casts: List[CastSchema]) -> List[Cast]:
        """Update the cast

        Args:
            casts (List[CastSchema]): 

        Raises:
            BadRequestError: Raise request when no id is found

        Returns:
            List[Cast]: 
        """
        _casts = []
        for cast in casts:
            db_obj = self.repository.get(cast.id)
            if not db_obj:
                raise BadRequestError(f"No cast with {cast.id} found")    
            _casts.append(self.repository.update(db_obj, cast))
        return _casts
    
    def delete(self, id):
        pass