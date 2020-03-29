#!/usr/bin/python3
"""contains the class definition of a State and an instance"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__":´
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
    .format(user, passwd, db), pool_pre_ping=True)
    
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session(engine)
for state in session.query(State).order_by(State.id).all(): 
    print("{}: {}".format(state.id, state.name))
session.close()