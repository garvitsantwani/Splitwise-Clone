from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship

from app.db.base import Base


class ExpenseSplit(Base):
    __tablename__ = "expense_splits"

    id: Mapped[int] = mapped_column(primary_key=True)

    expense_id: Mapped[int] = mapped_column(
        ForeignKey("expenses.id")
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    amount_owed: Mapped[float] = mapped_column()
    expense = relationship("Expense", back_populates="splits")
    user = relationship("User", back_populates="expense_splits")
    