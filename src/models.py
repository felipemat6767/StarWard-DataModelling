import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True, nullable=False)
    first_name =Column(String(25), nullable=False)
    last_name =Column(String(25), nullable=False)
    email =Column(String(30),unique=True, nullable=False) 
    password= Column(String(12), nullable=False)

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    Model = Column(String(250), nullable=False)
    vehicle_class = Column(String (250))
    cargo_capacity = Column(Integer)
    characters = relationship('Characters')
    characters_id = Column(Integer, ForeignKey('characters.id'))

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250))
    eye_color = Column(String(250))
    mass = Column(Integer)
    planets = relationship('Planets')
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    vehicles = relationship('Vehicles')
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    
class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer)
    terrain = Column(String(250))
    climate = Column(String(250))
    characters = relationship('Characters')
    characters_id = Column(Integer, ForeignKey('characters.id'))

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    favorite_planets = relationship('Planets')
    favorite_planets_id = Column(Integer, ForeignKey('planets.id'))
    favorite_vehicles = relationship('Vehicles')
    favorite_vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    favorite_characters = relationship('Characters')
    favorite_characters_id = Column(Integer, ForeignKey('characters.id'))
    user = relationship("User")
    user_id = Column(Integer, ForeignKey('user.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e