#!/usr/bin/python3
""" Prints with letter a """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database_name)
    engine = create_engine(db_url)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
