import uuid

from fastapi import HTTPException

from models.meal import Meal
from models.user import User
from services.unitofwork import IUnitOfWork
from schemas.meal import MealReadDTO, MealWriteDTO


class MealService:
    def __init__(self, current_user: User = None):
        self.current_user = current_user

    async def add(self, uow: IUnitOfWork, data: MealWriteDTO):
        async with uow:
            data = data.model_dump()
            data.update({"user_id": self.current_user.id})
            meal = await uow.meals.add(data)
            await uow.commit()
            return meal.to_dto()

    async def list(self, uow: IUnitOfWork):
        async with uow:
            meals = await uow.meals.list(where=(Meal.user == self.current_user,))
            return [meal.to_dto() for meal in meals]

    async def get(self, uow: IUnitOfWork, id: uuid.UUID):
        async with uow:
            meal = await uow.meals.get(id, where=(Meal.user == self.current_user,))
            if not meal:
                raise HTTPException(status_code=404, detail=f"Meal {id} not found")
            return meal.to_read_model()

    async def update(self, uow: IUnitOfWork, id: uuid.UUID, data: MealWriteDTO):
        async with uow:
            meal = await uow.meals.update(id, data.model_dump(), where=(Meal.user == self.current_user,))
            await uow.commit()
            if not meal:
                raise HTTPException(status_code=404, detail=f"Meal {id} not found")
            return meal.to_dto()

    async def delete(self, uow: IUnitOfWork, id: uuid.UUID):
        async with uow:
            meal = await uow.meals.delete(id, where=(Meal.user == self.current_user,))
            await uow.commit()
            if not meal:
                raise HTTPException(status_code=404, detail=f"Meal {id} not found")
            return meal.to_dto()
