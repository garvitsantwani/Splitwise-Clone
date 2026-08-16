from app.db.base import Base
from app.db.session import engine

from app.models.user import User
from app.models.group import Group
from app.models.group_member import GroupMember
from app.models.expense import Expense
from app.models.expense_split import ExpenseSplit


def create_tables():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
# Base → common foundation for all SQLAlchemy models

# User(Base) → tells SQLAlchemy User is a database model

# Base.metadata.create_all() → can create the corresponding tables