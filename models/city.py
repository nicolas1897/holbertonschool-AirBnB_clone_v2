#!/usr/bin/python3
"""
City module
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """
    Class City
    """

    __tablename__ = "cities"  #TODO change simple attr to table cities
    state_id = Column(
        String(60),
        nullable=False,
        ForeignKey('state.id')
    )
    name = Column(
        String(128),
        nullable=False
    )
