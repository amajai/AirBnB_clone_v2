#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from models.city import City
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel):
    """ State class """

    __tablename__ = 'states'

    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade="all,delete", backref="state")
    else:
        @property
        def cities(self):
            """Getter for cities property."""
            from models import storage
            cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
