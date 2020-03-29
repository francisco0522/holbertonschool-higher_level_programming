#!/usr/bin/python3
"""lists all State objects from the database"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from model_state import State


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    name = argv[4]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(user, passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana = State("Louisiana")
    session.add(louisiana)
    session.commit()
    session.close()