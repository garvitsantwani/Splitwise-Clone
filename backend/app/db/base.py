# base.py is very simple. Its main purpose is to create a common base for all the database models in our project.
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass



#   We made base.py because SQLAlchemy needs a common foundation for all our database model
# We're going to have many database tables:

# User       → users table
# Group      → groups table
# Expense     → expenses table
# Settlement  → settlements table

# Common parent for all database models.