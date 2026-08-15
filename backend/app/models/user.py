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
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

# This tells SQLAlchemy:
# User is a database model.
class User(Base):
    __tablename__ = "users"
    # The PostgreSQL table should be called users
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)





# users
# ┌────┬───────┬─────────────────┐
# │ id │ name  │ email           │
# ├────┼───────┼─────────────────┤
# │ 1  │ Rahul │ rahul@gmail.com │
# │ 2  │ Amit  │ amit@gmail.com   │
# └────┴───────┴─────────────────┘ 