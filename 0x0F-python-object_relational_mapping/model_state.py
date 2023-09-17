#!/usr/bin/python3
"""
Module to define the State class.
"""

from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class to link to the states table in the database.
    """
    __tablename__ = 'states'
    id = Column(Integer, Sequence('state_id_seq'), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
