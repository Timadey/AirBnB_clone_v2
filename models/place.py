#!/usr/bin/python3
""" Place Module for HBNB project """
from models.amenity import Amenity
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column('city_id', String(
        60), ForeignKey('cities.id'), nullable=False)
    user_id = Column('user_id', String(
        60), ForeignKey('users.id'), nullable=False)
    name = Column('name', String(128), nullable=False)
    description = Column('description', String(1024), nullable=True)
    number_rooms = Column('number_rooms', Integer, nullable=False, default=0)
    number_bathrooms = Column(
        'number_bathrooms', Integer, nullable=False, default=0)
    max_guest = Column('max_guest', Integer, nullable=False, default=0)
    price_by_night = Column('price_by_night', Integer,
                            nullable=False, default=0)
    latitude = Column('latitude', Float, nullable=True)
    longitude = Column('longitude', Integer, nullable=True)
    reviews = relationship('Review', uselist=True,
                           backref='place', cascade='all')
    place_amenity = Table('place_amenity', Base.metadata, Column('place_id', String(60), ForeignKey('places.id'), primary_key=True,
                          nullable=False), Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))
    amenities = relationship(
        'Amenity', secondary="place_amenity", viewonly=False)
    amenity_ids = []

    @property
    def reviews(self):
        """[For FileStorage] Return list of reviews for this place"""
        from models import storage
        review_store = storage.all()
        review_here = [
            review for review in review_store if review.place_id == self.place_id]
        return review_here

    @property
    def amenities(self):
        """[For FileStorage] Return list of amenities for this place"""
        from models import storage
        amenity_store = storage.all(Amenity)
        amenity_here = [
            amenity for amenity in amenity_store if amenity.id in self.amenity_id]
        return amenity_here

    @amenities.setter
    def amenities(self, amenity):
        if type(amenity) is Amenity:
            self.amenity_ids.append(amenity.id)
