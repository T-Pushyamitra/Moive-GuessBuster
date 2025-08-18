from fastapi import APIRouter, Depends, status
from src.core.settings import get_db, Session
from src.service.cast import CastService
from src.models.domain.cast import Cast
from src.models.schema.api_response import ApiResponse
from src.models.schema.cast import CastSchema, CastCreateSchema
from typing import List


router = APIRouter(prefix="/cast")

@router.get("/")
def get(db: Session = Depends(get_db)):
    service = CastService(db)
    casts = service.get_all()
    return ApiResponse[List[CastSchema]](status_code=status.HTTP_200_OK, 
                                         message=f"Found cast", data=casts)

@router.get("/{id}")
def get_by_id(id: int, db: Session = Depends(get_db)):
    service = CastService(db)
    cast = service.get_by_id(id)
    return ApiResponse[CastSchema](status_code=status.HTTP_200_OK, 
                                         message=f"Found cast", data=cast)

@router.get("/title/{title}")
def get_by_title(title: str, db: Session=Depends(get_db)):
    service = CastService(db)
    casts =service.get_by_title(title)
    return ApiResponse[List[CastSchema]](status_code=status.HTTP_200_OK, 
                                         message=f"Found cast", data=casts)
    

@router.post("/")
def create(casts: List[CastCreateSchema], db: Session = Depends(get_db)) -> ApiResponse:
    service = CastService(db)
    _casts = service.create(casts)
    data = [CastSchema.model_validate(cast) for cast in _casts]
    return ApiResponse[List[CastSchema]](status_code=status.HTTP_201_CREATED,
                                message=f"Created a cast : {casts}", data=data)

@router.post("/update")
def update(casts: List[CastSchema], db: Session = Depends(get_db)) -> ApiResponse:
    service = CastService(db)
    _casts = service.update(casts)
    data = [CastSchema.model_validate(cast) for cast in _casts]
    return ApiResponse[List[CastSchema]](status_code=status.HTTP_202_ACCEPTED,
                                message=f"Updated a cast : {casts}", data=data)