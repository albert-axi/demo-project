from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata)

class User(Base):
  __tablename__ = 'users'
  
  id = Column(Integer(), primary_key = True)
  username = Column(String())
  
class Playlist(Base):
  __tablename__ = 'playlists'
  
  id = Column(Integer(), primary_key = True)
  title = Column(String())
  user_id = Column(Integer(),ForeignKey('users.id'))

class Artist(Base):
  __tablename__ = 'artists'
  
  id = Column(Integer(), primary_key = True)
  name = Column(String())
  
class Song(Base):
  __tablename__ = 'songs'
  
  id = Column(Integer(), primary_key = True)
  title = Column(String())
  album = Column(String())
  artist_id = Column(Integer(),ForeignKey('artists.id'))