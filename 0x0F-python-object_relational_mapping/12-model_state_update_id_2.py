#!/usr/bin/python3
""" Add New_mexico"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_id = 2
    new_state_name = "New Mexico"

    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database_name)
    engine = create_engine(db_url)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(id=state_id).first()
    if state:
        state.name = new_state_name
        session.commit()

    session.close()
