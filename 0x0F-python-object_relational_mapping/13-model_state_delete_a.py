#!/usr/bin/python3

""" Delete state"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    letter_to_delete = "a"

    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database_name)
    engine = create_engine(db_url)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State).filter(State.name.like(f"%{letter_to_delete}%")).all()

    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()
