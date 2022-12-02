#!/usr/bin/python3
"""
Amenity module
"""
from models.base_model import BaseModel, Base
from sqlalquemy import Column, String


class Amenity(BaseModel, Base):
    """
    Class Amenity
    """

    __tablename__ = 'amenities' #TODO change simple attr to table amenities
    name = Column(
        String(128),
        nullable=False
    )
