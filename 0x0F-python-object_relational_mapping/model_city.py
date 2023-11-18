#!/usr/bin/python3

"""This model holds the State class for the table of states"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """The class City is a subclass of Base."""

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State', back_populates='cities')
