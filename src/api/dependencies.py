from typing import Annotated

from fastapi import Depends

from lib.user import current_active_user
from models.user import User
from services.unitofwork import IUnitOfWork, UnitOfWork

UOW = Annotated[IUnitOfWork, Depends(UnitOfWork)]
CurrentUser = Annotated[User, Depends(current_active_user)]

__all__ = ["UOW", "CurrentUser"]
