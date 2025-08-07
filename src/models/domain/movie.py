# from sqlalchemy import Column, Integer, String, Date
# from sqlalchemy.orm import relationship
# from app.core.database import Base
# from .association_tables import movie_cast_association

# class Movie(Base):
#     __tablename__ = "movie"
    
#     id = Column(Integer, primary_key=True)
#     name = Column(String, unique=True)
#     language = Column(String, nullable=False)
#     released_date = Column(Date, nullable=False)
#     dialogue = Column(String, nullable=False)
    
#     cast = relationship(
#         "Cast",
#         secondary=movie_cast_association,
#         back_populates="movies"
#     )
    
    