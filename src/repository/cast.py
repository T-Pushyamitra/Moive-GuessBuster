
from .base import BaseRepository
from src.models.domain.cast import Cast
from src.models.schema.cast import CastCreateSchema, CastSchema
from src.exception.custom_exception import BadRequestError
from typing import List

class CastRepository(BaseRepository[Cast]):
    
    def __init__(self, db):
        super().__init__(db, Cast)
        
    def get(self, id: int) -> Cast:
        """Get the cast by ID

        Args:
            id (int): 
        Returns:
            Cast:
        """
        return self.db.query(self.model).get(id)
    
    def get_all(self, limit: int, offset: int) -> List[Cast]:
        """Index of Cast

        Args:
            limit (int): 
            offset (int): 

        Returns:
            List[Cast]: 
        """
        return self.db.query(self.model).offset(offset).limit(limit).all()
    
    def create(self, cast: CastCreateSchema) -> Cast:
        """Create new Cast

        Args:
            cast (CastCreateSchema): 

        Raises:
            BadRequestError: Raise when the name already exists

        Returns:
            Cast: 
        """
        if bool(self.get_by_name(cast.name)):
            raise BadRequestError(f"Failed: Already cast with {cast.name} exists!")
        
        cast = self.model(**cast.model_dump())
        self.db.add(cast)
        self.db.commit()
        self.db.refresh(cast)
        return cast

    def update(self, cast: Cast, updatedCast: CastSchema) -> Cast:
        """Update the cast 

        Args:
            cast (Cast): 
            updatedCast (CastSchema): 

        Raises:
            BadRequestError: Raise when name is updated to existing one.

        Returns:
            Cast: 
        """
        for field in updatedCast.model_fields_set:
            model_dump = updatedCast.model_dump()
            if field == 'name' and self.get_by__name(model_dump[field]):
                raise BadRequestError(f"Failed: Already cast with {cast.name} exists!")
            setattr(cast, field, model_dump[field])
        self.db.commit()
        self.db.refresh(cast)
        return cast
    
    def delete(self, id):
        raise NotImplementedError("No service provided")