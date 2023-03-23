#!/usr/bin/python3
""" """
from os import getenv
from sqlalchemy import Column, Integer, String, create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """ """
    __engine = None
    __session = None

    def __init__(self):
        """create the engine"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine(
                'mysql+msqldb://{}:{}@{}/{}'
                .format(user, password, host, database), pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)

        if env == test:
            Base.metadata.drop_all(self.__engine)

    """Create a session to query the database"""
    self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                    expire_on_commit=False))

    def all(self, cls=None):
        """Query database session all objects depending of the class name"""
        obj_dict = {}
        classes = [User, State, City, Amenity, Place, Review]
        if cls is None:
            for cls in classes:
                for obj in self.__session.query(cls):
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    obj_dict[key] = obj
        else:
            for obj in self.__session.query(cls):
                key = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dict[key] = obj

        return obj_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj  if not None"""
        if obj is None:
            return
        else:
            session.delete(obj)
