import uuid
from datetime import datetime

from pydantic import BaseModel, Field, PositiveFloat
from sqlalchemy import DateTime


class WeightingBaseDTO(BaseModel):
    id: uuid.UUID
    created_at: datetime

    class Config:
        from_attributes = True


class WeightingWriteDTO(BaseModel):
    weight_kg: float = PositiveFloat()

    class Config:
        from_attributes = True


class WeightingReadDTO(WeightingWriteDTO, WeightingBaseDTO):
    pass
