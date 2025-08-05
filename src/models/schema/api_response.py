from typing import Optional, Generic, TypeVar
from pydantic.generics import GenericModel

Model = TypeVar("Model")

class ApiResponse(GenericModel, Generic[Model]):
    status_code: int
    message: Optional[str] = None
    data: Optional[Model] = None
    error_message: Optional[str] = None
    


