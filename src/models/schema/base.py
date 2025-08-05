from datetime import datetime

from pydantic import BaseModel
from pydantic_settings.main import ConfigDict


class BaseSchemaModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        populate_by_name=True
    )