#!/usr/bin/python3
'''
    Implementation of the State class
'''
from sqlalchemy import Column, Integer, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import os
import models


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            '''
            Cities getter
            '''
            city_list = []
            city_instance = models.storage.all(models.classes['City']).values()
            for val in city_instance:
                if val.state_id == self.id:
                    city_list.append(val)
            return city_list
