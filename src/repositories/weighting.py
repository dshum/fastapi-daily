from lib.repository import SQLAlchemyRepository
from models.weighting import Weighting


class WeightingRepository(SQLAlchemyRepository):
    model = Weighting
