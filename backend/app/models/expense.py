from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship

from app.db.base import Base


class Expense(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(primary_key=True)

    group_id: Mapped[int] = mapped_column(
        ForeignKey("groups.id")
    )

    paid_by: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    amount: Mapped[float] = mapped_column()

    description: Mapped[str] = mapped_column(
        String(255)
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
    group = relationship("Group", back_populates="expenses")
    payer = relationship("User", back_populates="expenses")
    splits = relationship("ExpenseSplit", back_populates="expense")