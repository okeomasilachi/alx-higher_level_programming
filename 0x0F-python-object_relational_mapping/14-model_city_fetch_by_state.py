#!/usr/bin/python3

"""prints all City objects from the database hbtn_0e_14_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    data = 'mysql+mysqldb://{}:{}@localhost:3306/{}'\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(data, pool_pre_ping=True)
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    ses = Session()
    c = ses.query(City, State).join(State).order_by(City.id).all()
    for city, state in c:
        print(f"{state.name}: ({city.id}) {city.name}")

    ses.close()
