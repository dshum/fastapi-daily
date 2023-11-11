import uuid
from datetime import datetime

from sqlalchemy import DateTime, func, UUID, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from lib.database import Base
from schemas.weighting import WeightingReadDTO


class Weighting(Base):
    __tablename__ = "weightings"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    weight_kg: Mapped[float] = mapped_column(Float(precision=1, asdecimal=True, decimal_return_scale=1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                                 server_default=func.now(), default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                                 server_default=func.now(), server_onupdate=func.now(),
                                                 default=func.now(), onupdate=func.now())
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    user = relationship("User", back_populates="weightings")

    def to_dto(self) -> WeightingReadDTO:
        return WeightingReadDTO(
            id=self.id,
            weight_kg=self.weight_kg,
            created_at=self.created_at,
        )
