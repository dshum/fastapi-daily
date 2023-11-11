import uuid
from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field


class WeightingBaseDTO(BaseModel):
    id: uuid.UUID
    created_at: datetime

    class Config:
        from_attributes = True


class WeightingWriteDTO(BaseModel):
    weight_kg: Decimal = Field(gt=0, max_digits=4, decimal_places=1)

    class Config:
        from_attributes = True


class WeightingReadDTO(WeightingWriteDTO, WeightingBaseDTO):
    pass
