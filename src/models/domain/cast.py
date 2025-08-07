from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship

from src.core.settings import Base
# from .association_tables import movie_cast_association

class Cast(Base):
    __tablename__ = "cast"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    title = Column(String, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    # movies = relationship(
    #     "Movie",
    #     secondary=movie_cast_association,
    #     back_populates="cast"
    # )