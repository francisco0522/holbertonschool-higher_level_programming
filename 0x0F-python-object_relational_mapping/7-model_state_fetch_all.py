#!/usr/bin/python3
"""lists all State objects from the database"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(user, passwd, db), pool_pre_ping=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
records = session.query(State).order_by(State.id).all()
for row in records:
    print("{}: {}".format(row.id, row.name))
session.close()
