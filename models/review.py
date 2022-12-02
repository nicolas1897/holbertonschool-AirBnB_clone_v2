#!/usr/bin/python3
"""
Review module
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """
    Class Review
    """

    __tablename__ = 'reviews'  #TODO change simple attr to table reviews
    place_id = Column(
        String(60),
        nullable=False,
        ForeignKey('places.id')
    )
    user_id = Column(
        String(60),
        nullable=False,
        ForeignKey('users.id')
    )
    text = Column(
        String(1024),
        nullable=False
    )
