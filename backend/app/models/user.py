# Because our Splitwise application needs users.
# And user.py will tell SQLAlchemy:
# "This is what a User looks like in our database."
# The users table will eventually store things like:
# id
# name
# email
# password_hash
# created_at
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column,relationship

from app.db.base import Base

# This tells SQLAlchemy:
# User is a database model.
class User(Base):
    __tablename__ = "users"
    # The PostgreSQL table should be called users
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    group_members = relationship("GroupMember", back_populates="user")
    expenses = relationship("Expense", back_populates="payer")
    expense_splits = relationship("ExpenseSplit", back_populates="user")

# It tells SQLAlchemy:
# "A User can have multiple GroupMember records."

# relationship("X") → Which model am I connected to?

# back_populates="Y" → What is the name of the relationship on the other model?




# users
# ┌────┬───────┬─────────────────┐
# │ id │ name  │ email           │
# ├────┼───────┼─────────────────┤
# │ 1  │ Rahul │ rahul@gmail.com │
# │ 2  │ Amit  │ amit@gmail.com   │
# └────┴───────┴─────────────────┘ 