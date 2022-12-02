#!/usr/bin/python3
"""
User module
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """
    Class User
    """

    __tablename__ = 'users'  #TODO change simple attr to table users
    first_name = Column(
        String(128),
        nullable=False
    )
    last_name = Column(
        String(128),
        nullable=False
    )
    email = Column(
        String(128),
        nullable=False
    )
    password = Column(
        String(128),
        nullable=False
    )
