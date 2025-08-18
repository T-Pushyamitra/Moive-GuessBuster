from .base import BaseSchemaModel

class __CastBase(BaseSchemaModel):
    name: str
    title: str  # e.g., Actor, Director
    model_config = {
        "from_attributes": True
    }
    
class CastCreateSchema(__CastBase):
    pass

class CastSchema(__CastBase):
    id: int
