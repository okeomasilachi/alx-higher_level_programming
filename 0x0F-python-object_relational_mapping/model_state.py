#!/usr/bin/python3

"""This model holds the State class for the table of states"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class State(Base):
    """The class State is a subclass of Base."""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state')
