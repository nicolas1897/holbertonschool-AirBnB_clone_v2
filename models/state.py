#!/usr/bin/python3
"""
State module
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """
    Class State
    """

    __tablename__ = 'states'  #TODO change simple attr to table states
    name = Column(
        String(128)
        nullable=False
    )
