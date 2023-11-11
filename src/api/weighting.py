import uuid
from typing import List

from fastapi import APIRouter, Depends

from api.dependencies import UOW, CurrentUser
from lib.user import current_active_user
from schemas.weighting import WeightingReadDTO, WeightingWriteDTO
from services.weighting import WeightingService

router = APIRouter(
    prefix="/weightings",
    tags=["Weightings"],
)


@router.post("/", response_model=WeightingReadDTO)
async def add(uow: UOW, current_user: CurrentUser, data: WeightingWriteDTO) -> WeightingReadDTO:
    return await WeightingService(current_user).add(uow, data)


@router.get("/", response_model=List[WeightingReadDTO])
async def list(uow: UOW, current_user: CurrentUser) -> list[WeightingReadDTO]:
    return await WeightingService(current_user).list(uow)


@router.get("/{id}", response_model=WeightingReadDTO)
async def get(uow: UOW, current_user: CurrentUser, id: uuid.UUID) -> WeightingReadDTO:
    return await WeightingService(current_user).get(uow, id)


@router.put("/{id}", response_model=WeightingReadDTO)
async def add(uow: UOW, current_user: CurrentUser, id: uuid.UUID, data: WeightingWriteDTO) -> WeightingReadDTO:
    return await WeightingService(current_user).update(uow, id, data)


@router.delete("/{id}", response_model=None)
async def add(uow: UOW, current_user: CurrentUser, id: uuid.UUID) -> None:
    return await WeightingService(current_user).delete(uow, id)
