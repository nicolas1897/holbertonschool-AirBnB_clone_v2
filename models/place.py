#!/usr/bin/python3
"""
Place module
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey


class Place(BaseModel, Base):
    """
    Class Place
    """

    __tablename__ = 'places'  #TODO change simple attr to table places
    city_id = Column(
        String(60),
        ForeignKey('cities.id'),
        nullable=False
    )
    user_id = Column(
        String(60),
        ForeignKey('users.id'),
        nullable=False
    )
    name = Column(
        String(128),
        nullable=False
    )
    description = Column(
        String(1024),
        nullable=True
    )
    number_rooms = Column(
        Integer,
        nullable=False,
        DefaultClause(0)
    )
    number_bathrooms = Column(
        Integer,
        nullable=False,
        DefaultClause(0)
    )
    max_guest = Column(
        Integer,
        nullable=False,
        DefaultClause(0)
    )
    price_by_night = Column(
        Integer,
        nullable=False,
        DefaultClause(0)
    )
    latitude = Column(
        Float,
        nullable=True
    )
    longitude = Column(
        Float,
        nullable=True
    )
    amenity_ids = Column(
        String(),
        nullable=False
    )
