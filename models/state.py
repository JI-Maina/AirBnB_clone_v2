#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):

    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), default="", nullable=False)
    cities = relationship("City", back_populates="state")

    @property
    def cities(self, id):
        c_list = []
        city = storage.all(City)
        for key, value in city.items():
            if value.state_id == id:
                c_list.append(value.name)
        return c_list
