import uuid
from typing import List

from fastapi import APIRouter, Depends

from api.dependencies import UOW, CurrentUser
from lib.user import current_active_user
from schemas.meal import MealReadDTO, MealWriteDTO
from services.meal import MealService

router = APIRouter(
    prefix="/meals",
    tags=["Meals"],
)


@router.post("/", response_model=MealReadDTO)
async def add(uow: UOW, current_user: CurrentUser, data: MealWriteDTO) -> MealReadDTO:
    return await MealService(current_user).add(uow, data)


@router.get("/", response_model=List[MealReadDTO])
async def list(uow: UOW, current_user: CurrentUser) -> list[MealReadDTO]:
    return await MealService(current_user).list(uow)


@router.get("/{id}", response_model=MealReadDTO)
async def get(uow: UOW, current_user: CurrentUser, id: uuid.UUID) -> MealReadDTO:
    return await MealService(current_user).get(uow, id)


@router.put("/{id}", response_model=MealReadDTO)
async def add(uow: UOW, current_user: CurrentUser, id: uuid.UUID, data: MealWriteDTO) -> MealReadDTO:
    return await MealService(current_user).update(uow, id, data)


@router.delete("/{id}", response_model=None)
async def add(uow: UOW, current_user: CurrentUser, id: uuid.UUID) -> None:
    return await MealService(current_user).delete(uow, id)
