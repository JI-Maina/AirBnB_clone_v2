#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):

    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), default="", nullable=False)
    cities = relationship("City", back_populates="state")
