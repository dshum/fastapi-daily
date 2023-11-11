import uuid
from datetime import datetime

from pydantic import BaseModel, Field


class MealBaseDTO(BaseModel):
    id: uuid.UUID
    created_at: datetime

    class Config:
        from_attributes = True


class MealWriteDTO(BaseModel):
    content: str = Field(min_length=5)

    class Config:
        from_attributes = True


class MealReadDTO(MealWriteDTO, MealBaseDTO):
    pass
