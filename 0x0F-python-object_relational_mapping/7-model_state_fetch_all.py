#!/usr/bin/python3
"""lists all State objects from the database"""

from sys import argv
from sqlalchemy import *
import warnings
from sqlalchemy import exc as sa_exc
from model_state import Base, State
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
states = session.query(State).all()
for model in states:
    print(model)
session.close()
