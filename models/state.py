#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column('name', String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """[For FileStorage] Returns the list of City in the State"""
        from models import storage
        # get all cities in the storage
        city_store = storage.all(City)
        # check for cities in this states
        cities_here = [city for city in city_store if city.state_id == self.id]
        return cities_here
