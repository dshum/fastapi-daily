import uuid
from datetime import datetime

from sqlalchemy import DateTime, func, UUID, Float, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from lib.database import Base
from schemas.meal import MealReadDTO


class Meal(Base):
    __tablename__ = "meals"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    user = relationship("User", back_populates="meals")

    def to_dto(self) -> MealReadDTO:
        return MealReadDTO(
            id=self.id,
            content=self.content,
            created_at=self.created_at,
        )
