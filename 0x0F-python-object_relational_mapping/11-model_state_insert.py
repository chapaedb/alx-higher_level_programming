#!/usr/bin/python3

""" Add new state"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    new_state_name = "Louisiana"

    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database_name)
    engine = create_engine(db_url)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name=new_state_name)
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
