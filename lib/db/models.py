from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata)

song_playlist = Table(
    'song_playlists',
    Base.metadata,
    Column('song_id', ForeignKey('songs.id'), primary_key=True),
    Column('playlist_id', ForeignKey('playlists.id'), primary_key=True),
    extend_existing=True,
)


class User(Base):
  __tablename__ = 'users'
  
  id = Column(Integer(), primary_key = True)
  username = Column(String())
  
  playlists = relationship('Playlist', backref=backref('user'))
  
  def __init__(self, username, id=None):
    self.username = username
    self.id = id
    
  def __repr__(self):
    return f"ID: {self.id} Username: {self.username}"
  
class Playlist(Base):
  __tablename__ = 'playlists'
  
  id = Column(Integer(), primary_key = True)
  title = Column(String())
  user_id = Column(Integer(),ForeignKey('users.id'))
  
  songs = relationship('Song', secondary=song_playlist, back_populates='playlists')
  
  def __init__(self, title, id=None):
    self.title = title
    self.id = id
    
  def __repr__(self):
    return f"ID: {self.id} Title: {self.title}"

class Artist(Base):
  __tablename__ = 'artists'
  
  id = Column(Integer(), primary_key = True)
  name = Column(String())
  
  songs = relationship('Song', backref=backref('artist'))
  
  def __init__(self, name, id=None):
    self.name = name
    self.id = id
    
  def __repr__(self):
    return f"ID: {self.id} Name: {self.name}"
  
class Song(Base):
  __tablename__ = 'songs'
  
  id = Column(Integer(), primary_key = True)
  title = Column(String())
  album = Column(String())
  artist_id = Column(Integer(),ForeignKey('artists.id'))
  
  playlists = relationship('Playlist', secondary=song_playlist, back_populates='songs')
  
  def __init__(self, title, album, id=None):
    self.title = title
    self.album = album
    self.id = id
    
  def __repr__(self):
    return f"ID: {self.id} Title: {self.title} Album: {self.album}"