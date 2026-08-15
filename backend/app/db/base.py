# base.py is very simple. Its main purpose is to create a common base for all the database models in our project.
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

# creates the common parent for all our database models.