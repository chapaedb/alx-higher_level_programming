#!/usr/bin/python3
"""State and Base class"""
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class State(Base):
    """
    State class that links to the states table in the database.

    Attributes:
        __tablename__ (str): The name of the table in the database.
        id (Column): An auto-generated, unique integer column serving as the primary key.
        name (Column): A string column with a maximum of 128 characters.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    from model_state import State

    Base.metadata.create_all(engine)
