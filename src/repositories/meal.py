from lib.repository import SQLAlchemyRepository
from models.meal import Meal


class MealRepository(SQLAlchemyRepository):
    model = Meal
