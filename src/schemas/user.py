import uuid
from datetime import datetime

from fastapi_users import schemas
from pydantic import Field
from sqlalchemy import DateTime


class UserReadDTO(schemas.BaseUser[uuid.UUID]):
    first_name: str = Field(min_length=1, max_length=255)
    last_name: str = Field(min_length=1, max_legth=255)
    created_at: datetime = Field(DateTime(timezone=True))


class UserCreateDTO(schemas.BaseUserCreate):
    first_name: str = Field(min_length=1, max_length=255)
    last_name: str = Field(min_length=1, max_length=255)


class UserUpdateDTO(schemas.BaseUserUpdate):
    first_name: str = Field(min_length=1, max_length=255)
    last_name: str = Field(min_length=1, max_length=255)
