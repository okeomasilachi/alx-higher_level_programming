#!/usr/bin/python3

"""prints the first State object from the database hbtn_0e_6_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    data = 'mysql+mysqldb://{}:{}@localhost:3306/{}'\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(data, pool_pre_ping=True)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    ses = Session()
    state = ses.query(State).filter(State.name.like("%a%")).all()
    for item in state:
        ses.delete(item)
    ses.commit()
    ses.close()
