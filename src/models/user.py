from datetime import datetime
from typing import List, TYPE_CHECKING

from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy import DateTime, func, String
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, relationship, mapped_column

from lib.database import Base, get_async_session

if TYPE_CHECKING:
    from models.weighting import Weighting
    from models.meal import Meal


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"

    first_name: Mapped[str] = mapped_column((String(255)))
    last_name: Mapped[str] = mapped_column((String(255)))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                                 server_default=func.now(), default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                                 server_default=func.now(), server_onupdate=func.now(),
                                                 default=func.now(), onupdate=func.now())
    weightings: Mapped[List["Weighting"]] = relationship("Weighting")
    meals: Mapped[List["Meal"]] = relationship("Meal")


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
