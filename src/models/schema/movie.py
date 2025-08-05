from typing import Optional, List
from datetime import date
from .base import BaseSchemaModel

class MovieBase(BaseSchemaModel):
    name: str
    released_date: date
    language: str
    dialogue: str

class MovieCreate(MovieBase):
    cast_ids: Optional[List[int]] = []

class MovieOut(MovieBase):
    id: int

    class Config:
        from_attributes = True

class CastInMovie(BaseSchemaModel):
    id: int
    name: str
    title: str

    class Config:
        orm_mode = True
        
class MovieWithCast(MovieOut):
    cast: List[CastInMovie] = []