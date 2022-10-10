#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

from models.base_model import Base
from models.state import State
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """
    The Database Storage Class
    """
    __engine = None
    __session = None

    def __init__(self) -> None:
        from sqlalchemy import create_engine, MetaData
        from os import getenv
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{passwd}@{host}:3306/{db}", pool_pre_ping=True)
        if env == 'test':
            metadata_obj = MetaData()
            metadata_obj.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on current session all object depending on the class"""
        if cls is None:
            # query all types of objects in the db
            all_cls = self.__session.query(
                User, State, City, Amenity, Place, Review).all()
        else:
            # query cls
            all_cls = self.__session.query(cls).all()
        # add each object to the dictionary and return
        all_obj = {}
        for each_obj in all_cls:
            key = f"{each_obj.__class__}.{each_obj.id}"
            all_obj[key] = each_obj
        return all_obj

    def new(self, obj):
        """Add obj to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database seesion"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initiate a session"""
        Base.metadata.create_all(self.__engine)
        from sqlalchemy.orm import sessionmaker, scoped_session
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()
