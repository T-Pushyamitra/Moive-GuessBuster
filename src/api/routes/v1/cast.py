from fastapi import APIRouter, Depends
from src.models.schema.cast import CastCreate, CastOut
from src.core.settings import get_db, Session
from src.service.cast import CastService

router = APIRouter()


@router.post("/")
def create(cast: CastCreate, db: Session = Depends(get_db)):
    service = CastService(db)
    return service.create(cast.dict())


@router.get("/{id}")
def create(id: int, db: Session = Depends(get_db)):
    service = CastService(db)
    return service.get(id)

