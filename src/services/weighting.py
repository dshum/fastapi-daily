import uuid

from fastapi import HTTPException

from models.user import User
from models.weighting import Weighting
from services.unitofwork import IUnitOfWork
from schemas.weighting import WeightingReadDTO, WeightingWriteDTO


class WeightingService:
    def __init__(self, current_user: User = None):
        self.current_user = current_user

    async def add(self, uow: IUnitOfWork, data: WeightingWriteDTO):
        async with uow:
            data = data.model_dump()
            data.update({"user_id": self.current_user.id})
            weighting = await uow.weightings.add(data=data)
            await uow.commit()
            return weighting.to_dto()

    async def list(self, uow: IUnitOfWork):
        async with uow:
            weightings = await uow.weightings.list(where=(Weighting.user == self.current_user,))
            return [weighting.to_dto() for weighting in weightings]

    async def get(self, uow: IUnitOfWork, id: uuid.UUID):
        async with uow:
            weighting = await uow.weightings.get(id, where=(Weighting.user == self.current_user,))
            if not weighting:
                raise HTTPException(status_code=404, detail=f"Weighting {id} not found")
            return weighting.to_dto()

    async def update(self, uow: IUnitOfWork, id: uuid.UUID, data: WeightingWriteDTO):
        async with uow:
            weighting = await uow.weightings.update(id, data.model_dump(), where=(Weighting.user == self.current_user,))
            await uow.commit()
            if not weighting:
                raise HTTPException(status_code=404, detail=f"Weighting {id} not found")
            return weighting

    async def delete(self, uow: IUnitOfWork, id: uuid.UUID):
        async with uow:
            weighting = await uow.weightings.delete(id, where=(Weighting.user == self.current_user,))
            await uow.commit()
            if not weighting:
                raise HTTPException(status_code=404, detail=f"Weighting {id} not found")
            return weighting
