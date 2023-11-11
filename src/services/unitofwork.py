from abc import ABC, abstractmethod

from lib.database import async_session_maker
from lib.repository import AbstractRepository
from repositories.meal import MealRepository
from repositories.weighting import WeightingRepository


class IUnitOfWork(ABC):
    weightings: AbstractRepository
    meals: AbstractRepository

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, *args):
        raise NotImplementedError

    @abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError


class UnitOfWork:
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()
        self.weightings = WeightingRepository(self.session)
        self.meals = MealRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
