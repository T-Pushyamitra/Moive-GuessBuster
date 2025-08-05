from .base import BaseSchemaModel

class __CastBase(BaseSchemaModel):
    name: str
    title: str  # e.g., Actor, Director

class CastCreate(__CastBase):
    pass

class CastOut(__CastBase):
    id: int

    class Config:
        orm_mode = True
