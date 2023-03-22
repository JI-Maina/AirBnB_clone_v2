#!/usr/bin/python3
""" """
from os import getenv

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
                .format(user, password, host,database), pool_pre_ping=True)

        if env == test:
            Base.metadate.Drop_all(__engine)
