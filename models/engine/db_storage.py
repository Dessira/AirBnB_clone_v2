#!/usr/bin/python3
'''This module implements the class DBStorage'''

class DBStorage:
    '''Implementation of DBStorage class'''
    __engine = None
    __session = None

    def __init__(self):
        from sqlalchemy import create_engine
        from os import environ
        user = environ["HBNB_MYSQL_USER"]
        password = environ["HBNB_MYSQL_PWD"]
        host = environ["HBNB_MYSQL_HOST"]
        database = environ["HBNB_MYSQL_DB"]
        engine = create_engine("mysql+mysqldb://{}:\
                {}@{}:{}".format(user, password, host, \
                database), pool_pre_ping=True)

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
