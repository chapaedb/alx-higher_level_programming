#!/usr/bin/python3
"""Class definitions"""
import sys
from sqlalchemy import create_engine, Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

class State(Base):
    _table_name_='states'
    id = Column(Integer, Primary_Key = True, Unique = True,auto_increment = True,nullable = False)
    name = Column(String(128),nullable = False)
Base.metadata.create_all(engine)
